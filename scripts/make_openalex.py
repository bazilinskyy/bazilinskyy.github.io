# by Pavlo Bazilinskyy <pavlo.bazilinskyy@gmail.com>
# Builds the data the site takes from OpenAlex (free, no key), run nightly by
# .github/workflows/nightly.yml; by hand:
#   python3 scripts/make_openalex.py
# - _data/citations.json: citation count of each _publications/*.md, looked up by its doi:
#   (publication pages)
# - _data/coauthor_institutions.json: the institutions of my co-authors with their location, number
#   of joint works and the people, each linked to their website (map on the about page)
import collections
import glob
import json
import os
import re
import urllib.parse
import urllib.request

ORCID = '0000-0001-9565-8240'
API = 'https://api.openalex.org'
BATCH = 50  # OpenAlex takes up to 50 values in one filter
# co-author names as OpenAlex spells them -> as the map lists them (variants, scripts, initials)
NAMES = {
    'Christian Janssen': 'Christian P. Janssen',
    'M.H. Martens': 'Marieke H. Martens',
    'Marieke Martens': 'Marieke H. Martens',
    'Γεώργιος Παπαϊωάννου': 'Georgios Papaioannou',
    'V. Onkhar': 'Vishal Onkhar',
    'Angel Hsing‐Chi Hwang': 'Angel Hsing-Chi Hwang',
    'Md Shadab Alam': 'Shadab Alam',
}
# co-authors OpenAlex also puts at institutions they were not at for our papers -> their one institution
PLACE = {
    'Shadab Alam': 'Eindhoven University of Technology',
}


def get(path, **params):
    with urllib.request.urlopen(f'{API}/{path}?{urllib.parse.urlencode(params)}', timeout=60) as r:
        return json.load(r)


def short(openalex_id):
    return openalex_id.rsplit('/', 1)[-1]


def dois():
    """{lowercase doi: publication name} of the publications with a doi."""
    out = {}
    for path in sorted(glob.glob('_publications/*.md')):
        m = re.search(r'^doi:\s*["\']?([^"\'\s]+)', open(path, encoding='utf-8').read(), re.MULTILINE)
        if m:
            out[m.group(1).lower()] = os.path.basename(path)[:-3]
    return out


def citations(by_doi):
    """{publication name: {count, openalex}} of the works OpenAlex knows and that are cited at least once."""
    out, keys = {}, list(by_doi)
    for i in range(0, len(keys), BATCH):
        for work in get('works', filter='doi:' + '|'.join(keys[i:i + BATCH]), **{'per-page': BATCH},
                        select='id,doi,cited_by_count')['results']:
            name = by_doi.get((work['doi'] or '').removeprefix('https://doi.org/').lower())
            if name and work['cited_by_count']:
                out[name] = dict(count=work['cited_by_count'], openalex=short(work['id']))
    return dict(sorted(out.items()))


def my_works():
    """All works with my ORCID (id, authorships)."""
    works, cursor = [], '*'
    while cursor:
        page = get('works', filter=f'author.orcid:{ORCID}', **{'per-page': 200}, cursor=cursor,
                   select='id,authorships')
        works += page['results']
        cursor = page['meta'].get('next_cursor') if page['results'] else None
    return works


def best_url(urls):
    """The most personal of a researcher's ORCID links [(label, url)]: own site, then a staff page, then the rest."""
    def rank(item):
        text = ' '.join(item).lower()
        if any(w in text for w in ('linkedin', 'researchgate', 'twitter', 'x.com', 'facebook', 'scholar.google')):
            return 3
        if any(w in text for w in ('personal', 'homepage', 'home page', 'website', 'portfolio', 'github.io')):
            return 0
        return 1 if any(w in text for w in ('profile', 'staff', 'university', 'research.')) else 2
    return min(urls, key=rank)[1] if urls else None


def manual_urls():
    """{name: url} of the hand-written _data/collaborators.yml (titles dropped), which win over ORCID."""
    out, name = {}, None
    for line in open('_data/collaborators.yml', encoding='utf-8'):
        if m := re.match(r'-\s*name:\s*(.+)', line):
            name = re.sub(r'^(Dr\.|Prof\.|Dr|Prof)\s+', '', m.group(1).strip().strip('"\''))
            name = NAMES.get(name, name)  # as the map spells it
        elif (m := re.match(r'\s+name_url:\s*(\S+)', line)) and name:
            out[name] = m.group(1).strip('"\'')
    return out


def link(name, orcid, author, manual):
    """Where a co-author's name links to: my own list, their ORCID website, their ORCID page, their OpenAlex page."""
    if name in manual:
        return manual[name]
    if orcid:
        try:
            req = urllib.request.Request(f'https://pub.orcid.org/v3.0/{short(orcid)}/researcher-urls', headers={'Accept': 'application/json'})
            with urllib.request.urlopen(req, timeout=30) as r:
                urls = [(u.get('url-name') or '', u['url']['value']) for u in json.load(r).get('researcher-url') or []]
            return best_url(urls) or orcid
        except (OSError, ValueError, KeyError):
            return orcid
    return author


def collaborators(works, url=None):
    """[{name, city, country, lat, lon, works, people: [{name, url}]}] of my co-authors' institutions, most joint
    works first. url(name, orcid, openalex author) gives the link of a person (link() with manual_urls() by default)."""
    if url is None:
        manual = manual_urls()
        url = lambda name, orcid, author: link(name, orcid, author, manual)
    joint, people, names, who = collections.defaultdict(set), collections.defaultdict(set), {}, {}
    for work in works:
        for a in work['authorships']:
            if (a['author'].get('orcid') or '').endswith(ORCID):
                continue  # my own affiliations
            name = NAMES.get(a['author']['display_name'], a['author']['display_name'])
            if not who.get(name, (None,))[0]:  # of the spellings of one person, the one with an ORCID
                who[name] = (a['author'].get('orcid'), a['author'].get('id'))
            for inst in a['institutions']:
                if PLACE.get(name, inst['display_name']) != inst['display_name']:
                    continue
                joint[inst['id']].add(work['id'])
                people[inst['id']].add(name)
                names[inst['id']] = inst['display_name']
    ids, geo = list(joint), {}
    for i in range(0, len(ids), BATCH):
        for inst in get('institutions', filter='openalex:' + '|'.join(short(x) for x in ids[i:i + BATCH]),
                        **{'per-page': BATCH}, select='id,geo')['results']:
            geo[inst['id']] = inst['geo']
    links = {n: url(n, *who[n]) for n in who}
    out = [dict(name=names[i], city=geo[i]['city'], country=geo[i]['country'], lat=round(geo[i]['latitude'], 3),
                lon=round(geo[i]['longitude'], 3), works=len(joint[i]),
                people=[dict(name=n, url=links[n]) for n in sorted(people[i])])
           for i in ids if geo.get(i) and geo[i].get('latitude') is not None]
    return sorted(out, key=lambda c: (-c['works'], c['name']))


def write(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _check():
    assert best_url([('LinkedIn', 'l'), ('TU Delft staff page', 's'), ('Personal Website', 'p')]) == 'p'
    assert best_url([('LinkedIn', 'l'), ('Delft University of Technology profile page', 's')]) == 's' and best_url([]) is None
    me, other = {'orcid': f'https://orcid.org/{ORCID}', 'display_name': 'Me'}, {'orcid': None, 'display_name': 'Ann'}
    other2 = {'orcid': None, 'display_name': 'M.H. Martens'}  # two spellings of one person count once
    shadab = {'orcid': None, 'display_name': 'Md Shadab Alam'}  # only at the institution in PLACE
    inst = [{'id': 'I1', 'display_name': 'Uni'}]
    works = [{'id': 'W1',
              'authorships': [{'author': me, 'institutions': inst}, {'author': other, 'institutions': inst},
                              {'author': other2, 'institutions': inst}, {'author': dict(other2, display_name='Marieke Martens'), 'institutions': inst},
                              {'author': shadab, 'institutions': [{'id': 'I3', 'display_name': 'Elsewhere'}]}]},
             {'id': 'W2',
              'authorships': [{'author': me, 'institutions': [{'id': 'I2', 'display_name': 'Mine'}]}]}]
    global get
    real, get = get, lambda path, **p: {'results': [{'id': 'I1', 'geo': {'city': 'C', 'country': 'X', 'latitude': 1.0, 'longitude': 2.0}}]}
    try:  # only the co-author's institution counts, not mine
        people = [dict(name='Ann', url='u:Ann'), dict(name='Marieke H. Martens', url='u:Marieke H. Martens')]
        assert collaborators(works, url=lambda n, o, a: f'u:{n}') == [dict(name='Uni', city='C', country='X', lat=1.0, lon=2.0, works=1, people=people)]
    finally:
        get = real


if __name__ == '__main__':
    _check()
    by_doi = dois()
    cites = citations(by_doi)
    write('_data/citations.json', cites)
    works = my_works()
    collab = collaborators(works)
    write('_data/coauthor_institutions.json', collab)
    print(f'citations: {len(cites)} of {len(by_doi)} publications with a doi cited; {len(works)} works, '
          f'{len(collab)} collaborating institutions')
