# by Pavlo Bazilinskyy <pavlo.bazilinskyy@gmail.com>
# Builds _data/citations.json, the citation counts the publication pages show: OpenAlex
# (free, no key) looked up by the doi: of each _publications/*.md. Run nightly by
# .github/workflows/nightly.yml; by hand:
#   python3 scripts/make_citations.py
import glob
import json
import os
import re
import urllib.parse
import urllib.request

OUT = '_data/citations.json'
BATCH = 50  # OpenAlex takes up to 50 values in one filter


def dois():
    """{lowercase doi: publication name} of the publications with a doi."""
    out = {}
    for path in sorted(glob.glob('_publications/*.md')):
        m = re.search(r'^doi:\s*["\']?([^"\'\s]+)', open(path, encoding='utf-8').read(), re.MULTILINE)
        if m:
            out[m.group(1).lower()] = os.path.basename(path)[:-3]
    return out


def counts(by_doi):
    """{publication name: {count, openalex}} of the works OpenAlex knows and that are cited at least once."""
    out, keys = {}, list(by_doi)
    for i in range(0, len(keys), BATCH):
        query = urllib.parse.urlencode({'filter': 'doi:' + '|'.join(keys[i:i + BATCH]), 'per-page': BATCH,
                                        'select': 'id,doi,cited_by_count'})
        with urllib.request.urlopen(f'https://api.openalex.org/works?{query}', timeout=60) as r:
            for work in json.load(r)['results']:
                name = by_doi.get((work['doi'] or '').removeprefix('https://doi.org/').lower())
                if name and work['cited_by_count']:
                    out[name] = dict(count=work['cited_by_count'], openalex=work['id'].rsplit('/', 1)[1])
    return dict(sorted(out.items()))


if __name__ == '__main__':
    by_doi = dois()
    data = counts(by_doi)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f'{OUT}: {len(data)} of {len(by_doi)} publications with a doi cited, {sum(v["count"] for v in data.values())} citations')
