# by Pavlo Bazilinskyy <pavlo.bazilinskyy@gmail.com>
# Builds _data/latest_publications.json, the newest publications in the sidebar of the home page.
# Publications have a year but no date, so "newest" is the day each _publications/*.md was
# first committed (git history), then the year. Run nightly by .github/workflows/nightly.yml
# (which checks out the full history for it); by hand:
#   python3 scripts/make_latest_publications.py
import glob
import json
import os
import re
import subprocess

SHOW = 3
OUT = '_data/latest_publications.json'


def field(text, name):
    m = re.search(rf'^{name}:\s*(.+)$', text, re.MULTILINE)
    return m.group(1).strip().strip('"\'') if m else ''


def venue(display):
    """A short venue: the acronym in brackets (AutoUI), else the part before the first comma (the journal)."""
    m = re.search(r'\(([A-Za-z][\w\-]*)\)', display)
    v = m.group(1) if m else display.split(',')[0].strip().rstrip('.')
    return v if len(v) <= 45 else v[:45].rsplit(' ', 1)[0] + '…'  # a few proceedings have no acronym


def added(path):
    """Day the file was first committed ('' if it is not committed yet)."""
    days = subprocess.run(['git', 'log', '--diff-filter=A', '--format=%as', '--', path], capture_output=True, text=True).stdout.split()
    return days[-1] if days else ''


def latest(pubs):
    """The SHOW newest of [{name, title, image, venue, year, added}]: last added first, then the later year."""
    return sorted(pubs, key=lambda p: (p['added'], p['year'], p['name']), reverse=True)[:SHOW]


def _check():
    pubs = [dict(name='a', year='2025', added='2026-09-01'), dict(name='b', year='2026', added='2026-09-01'),
            dict(name='c', year='2026', added='2026-08-01'), dict(name='d', year='2024', added='2026-10-01')]
    assert [p['name'] for p in latest(pubs)] == ['d', 'b', 'a']
    assert venue('Adjunct Proceedings of the 18th AutomotiveUI Conference (AutoUI). Gothenburg, Sweden') == 'AutoUI'
    assert venue('Applied Ergonomics, 95, 103450') == 'Applied Ergonomics'
    assert venue('Submitted for publication.') == 'Submitted for publication' and len(venue('x ' * 40)) <= 46


if __name__ == '__main__':
    _check()
    pubs = []
    for path in glob.glob('_publications/*.md'):
        text = open(path, encoding='utf-8').read()
        pubs.append(dict(name=os.path.basename(path)[:-3], title=field(text, 'title'), image=field(text, 'image'),
                         venue=venue(field(text, 'display')), year=field(text, 'year'), added=added(path)))
    data = latest(pubs)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"{OUT}: {', '.join(p['name'] for p in data)}")
