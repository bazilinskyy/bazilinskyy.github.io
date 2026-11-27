# Builds _data/bib.json from the BibTeX entries _publications/<name>.txt, so pages can use what
# only the BibTeX holds: full author names, the journal or proceedings name without the place,
# volume, issue and pages (Google Scholar tags on the publication pages,
# _includes/publication-meta.html). Run nightly by .github/workflows/nightly.yml; by hand:
#   python3 scripts/make_bib_data.py
import glob
import json
import os
import re
import unicodedata

FIELDS = ('journal', 'booktitle', 'volume', 'number', 'pages', 'publisher', 'school', 'institution')
ACCENT = {"'": '\u0301', '`': '\u0300', '^': '\u0302', '"': '\u0308', '~': '\u0303', '=': '\u0304',
          '.': '\u0307', 'u': '\u0306', 'v': '\u030c', 'H': '\u030b', 'c': '\u0327'}


def delatex(s):
    s = re.sub(r'\\([`\'^"~=.]|[uvHc](?=[\s{]))\s*\{?\\?([a-zA-Z])\}?',
               lambda m: unicodedata.normalize('NFC', m.group(2) + ACCENT[m.group(1)]), s)
    s = re.sub(r'\\([&%$_#])', r'\1', s).replace('{', '').replace('}', '')
    return re.sub(r'\s+', ' ', s).strip()


def parse(text):
    """(type, {field: value}) of one entry; values may hold nested braces."""
    head = re.search(r'@(\w+)\s*\{\s*[^,\s]+\s*,', text)
    if not head:
        return None, {}
    fields, i = {}, head.end()
    for m in re.finditer(r'(\w+)\s*=\s*', text[i:]):
        j = i + m.end()
        if j >= len(text):
            break
        if text[j] == '{':
            depth, k = 0, j
            while k < len(text):
                depth += {'{': 1, '}': -1}.get(text[k], 0)
                if depth == 0:
                    break
                k += 1
            value = text[j + 1:k]
        elif text[j] == '"':
            value = text[j + 1:text.index('"', j + 1)]
        else:
            value = re.match(r'[^,}\s]*', text[j:]).group(0)
        fields.setdefault(m.group(1).lower(), delatex(value))
    return head.group(1).lower(), fields


def entry(text):
    kind, f = parse(text)
    if not kind:
        return None
    out = dict(type=kind, authors=[a.strip() for a in re.split(r'\s+and\s+', f.get('author', '')) if a.strip()])
    out.update({k: f[k] for k in FIELDS if f.get(k)})
    if f.get('pages'):
        first, _, last = f['pages'].replace('\u2013', '-').partition('-')
        out['firstpage'], out['lastpage'] = first.strip(), last.strip('- ')
    return out


def _check():
    e = entry('@article{x,\n  title={T},\n  author={Kov{\\\'a}csov{\\\'a}, Nat{\\\'a}lia and De Winter, J. C. F.},\n'
              '  journal={Procedia Manufacturing},\n  volume={3},\n  pages={2534--2542},\n  year={2015}\n}')
    assert e['authors'] == ['Kovácsová, Natália', 'De Winter, J. C. F.'], e
    assert (e['journal'], e['volume'], e['firstpage'], e['lastpage']) == ('Procedia Manufacturing', '3', '2534', '2542'), e


if __name__ == '__main__':
    _check()
    data = {}
    for path in sorted(glob.glob('_publications/*.txt')):
        e = entry(open(path, encoding='utf-8').read())
        if e:
            data[os.path.basename(path)[:-4]] = e
    with open('_data/bib.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(f'bib data: {len(data)} entries')
