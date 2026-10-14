# by Pavlo Bazilinskyy <pavlo.bazilinskyy@gmail.com>
# Builds the data the site takes from OpenAlex (free, no key), run nightly by
# .github/workflows/nightly.yml; by hand:
#   python3 scripts/make_openalex.py
# - _data/citations.json: citation count of each _publications/*.md, looked up by its doi:
#   (publication pages)
# - _data/coauthor_institutions.json: the institutions of my co-authors with their location, number
#   of joint works and names (map on the about page)
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


def collaborators(works):
    """[{name, city, country, lat, lon, works, people}] of my co-authors' institutions, most joint works first."""
    joint, people, names = collections.defaultdict(set), collections.defaultdict(set), {}
    for work in works:
        for a in work['authorships']:
            if (a['author'].get('orcid') or '').endswith(ORCID):
                continue  # my own affiliations
            for inst in a['institutions']:
                joint[inst['id']].add(work['id'])
                name = a['author']['display_name']
                people[inst['id']].add(NAMES.get(name, name))
                names[inst['id']] = inst['display_name']
    ids, geo = list(joint), {}
    for i in range(0, len(ids), BATCH):
        for inst in get('institutions', filter='openalex:' + '|'.join(short(x) for x in ids[i:i + BATCH]),
                        **{'per-page': BATCH}, select='id,geo')['results']:
            geo[inst['id']] = inst['geo']
    out = [dict(name=names[i], city=geo[i]['city'], country=geo[i]['country'], lat=round(geo[i]['latitude'], 3),
                lon=round(geo[i]['longitude'], 3), works=len(joint[i]), people=sorted(people[i]))
           for i in ids if geo.get(i) and geo[i].get('latitude') is not None]
    return sorted(out, key=lambda c: (-c['works'], c['name']))


def write(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _check():
    me, other = {'orcid': f'https://orcid.org/{ORCID}', 'display_name': 'Me'}, {'orcid': None, 'display_name': 'Ann'}
    other2 = {'orcid': None, 'display_name': 'M.H. Martens'}  # two spellings of one person count once
    inst = [{'id': 'I1', 'display_name': 'Uni'}]
    works = [{'id': 'W1',
              'authorships': [{'author': me, 'institutions': inst}, {'author': other, 'institutions': inst},
                              {'author': other2, 'institutions': inst}, {'author': dict(other2, display_name='Marieke Martens'), 'institutions': inst}]},
             {'id': 'W2',
              'authorships': [{'author': me, 'institutions': [{'id': 'I2', 'display_name': 'Mine'}]}]}]
    global get
    real, get = get, lambda path, **p: {'results': [{'id': 'I1', 'geo': {'city': 'C', 'country': 'X', 'latitude': 1.0, 'longitude': 2.0}}]}
    try:  # only the co-author's institution counts, not mine
        assert collaborators(works) == [dict(name='Uni', city='C', country='X', lat=1.0, lon=2.0, works=1, people=['Ann', 'Marieke H. Martens'])]
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
