# by Pavlo Bazilinskyy <pavlo.bazilinskyy@gmail.com>
# Builds the data the site takes from OpenAlex (free, no key), run nightly by
# .github/workflows/nightly.yml; by hand:
#   python3 scripts/make_openalex.py
# - _data/citations.json: citation count of each _publications/*.md, looked up by its doi:
#   (publication pages)
# - _data/citations_per_year.json: citations received per year by all works with my ORCID,
#   summed from each work's counts_by_year (publications page). Not the author's own
#   counts_by_year: OpenAlex fills that by year of publication, not of citation.
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
    """All works with my ORCID (id, counts_by_year, authorships)."""
    works, cursor = [], '*'
    while cursor:
        page = get('works', filter=f'author.orcid:{ORCID}', **{'per-page': 200}, cursor=cursor,
                   select='id,counts_by_year,authorships')
        works += page['results']
        cursor = page['meta'].get('next_cursor') if page['results'] else None
    return works


def per_year(works):
    """[{year, count}] of the citations received per year."""
    years = collections.Counter()
    for work in works:
        for y in work['counts_by_year']:
            years[y['year']] += y['cited_by_count']
    return [dict(year=y, count=n) for y, n in sorted(years.items())]


def collaborators(works):
    """[{name, city, country, lat, lon, works, people}] of my co-authors' institutions, most joint works first."""
    joint, people, names = collections.defaultdict(set), collections.defaultdict(set), {}
    for work in works:
        for a in work['authorships']:
            if (a['author'].get('orcid') or '').endswith(ORCID):
                continue  # my own affiliations
            for inst in a['institutions']:
                joint[inst['id']].add(work['id'])
                people[inst['id']].add(a['author']['display_name'])
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
    inst = [{'id': 'I1', 'display_name': 'Uni'}]
    works = [{'id': 'W1', 'counts_by_year': [{'year': 2024, 'cited_by_count': 2}],
              'authorships': [{'author': me, 'institutions': inst}, {'author': other, 'institutions': inst}]},
             {'id': 'W2', 'counts_by_year': [{'year': 2024, 'cited_by_count': 1}, {'year': 2025, 'cited_by_count': 4}],
              'authorships': [{'author': me, 'institutions': [{'id': 'I2', 'display_name': 'Mine'}]}]}]
    assert per_year(works) == [{'year': 2024, 'count': 3}, {'year': 2025, 'count': 4}]
    global get
    real, get = get, lambda path, **p: {'results': [{'id': 'I1', 'geo': {'city': 'C', 'country': 'X', 'latitude': 1.0, 'longitude': 2.0}}]}
    try:  # only the co-author's institution counts, not mine
        assert collaborators(works) == [dict(name='Uni', city='C', country='X', lat=1.0, lon=2.0, works=1, people=['Ann'])]
    finally:
        get = real


if __name__ == '__main__':
    _check()
    by_doi = dois()
    cites = citations(by_doi)
    write('_data/citations.json', cites)
    works = my_works()
    years = per_year(works)
    write('_data/citations_per_year.json', years)
    collab = collaborators(works)
    write('_data/coauthor_institutions.json', collab)
    print(f'citations: {len(cites)} of {len(by_doi)} publications with a doi cited; {len(works)} works, '
          f'{sum(y["count"] for y in years)} citations in {len(years)} years; {len(collab)} collaborating institutions')
