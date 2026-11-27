# Fetches the logo of each outlet in _data/media.yml (the largest icon its website declares:
# apple-touch-icon, then icon links, then /favicon.ico) into images/media/<slug>.png, shown in
# the "In the news" box of the sidebar. Outlets that already have one are skipped, so rerun it
# after adding coverage (needs macOS sips to convert and resize; by hand, not nightly):
#   python3 scripts/make_media_logos.py
# An outlet without a logo shows its "short:" text from media.yml, else its first letter.
# Some sites need a hand-picked file (Der Standard, BREAKIT): save it as images/media/<slug>.png.
import html.parser
import os
import re
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(__file__))
from make_talk_map import entries  # the same flat YAML reader

OUT = 'images/media'
SIZE = 64
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36'}
# outlets whose link is not on their own site, or that have none
SITE = {
    'BBC Global News Podcast': 'https://www.bbc.com',
    'Sveriges Radio': 'https://sverigesradio.se',
    'Las Provincias': 'https://www.lasprovincias.es',
}


# outlets shown as text instead: their site shows another brand (CyclingTips became Velo), or
# its icon is too small or unclear (WIRED, BBC, Sveriges Radio: "short:" in media.yml)
NONE = {'CyclingTips', 'WIRED', 'BBC Future', 'BBC Global News Podcast', 'Sveriges Radio'}


def slug(outlet, url=''):
    """File name of an outlet's logo; an outlet named in another script goes by its website."""
    s = re.sub(r'[^a-z0-9]+', '-', outlet.lower()).strip('-')
    if not s and url:
        s = re.sub(r'[^a-z0-9]+', '-', urllib.parse.urlparse(url).netloc.removeprefix('www.')).strip('-')
    return s


class Icons(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.found = []  # (score, href)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        rel = (a.get('rel') or '').lower()
        if tag != 'link' or 'icon' not in rel or not a.get('href'):
            return
        size = max([int(n) for n in re.findall(r'(\d+)x\d+', a.get('sizes') or '')] or [0])
        score = (2 if 'apple-touch' in rel else 1) * 1000 + size - (500 if a['href'].endswith('.svg') else 0)
        self.found.append((score, a['href']))


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return r.geturl(), r.read()


def logo(site, dest):
    base, page = get(site)
    p = Icons()
    p.feed(page.decode('utf-8', 'ignore'))
    for _, href in sorted(p.found, reverse=True) + [(0, '/favicon.ico')]:
        try:
            _, data = get(urllib.parse.urljoin(base, href))
        except Exception:
            continue
        with tempfile.NamedTemporaryFile(suffix=os.path.splitext(href.split('?')[0])[1] or '.ico') as f:
            f.write(data)
            f.flush()
            r = subprocess.run(['sips', '-s', 'format', 'png', '-Z', str(SIZE), f.name, '--out', dest], capture_output=True)
            if r.returncode == 0 and os.path.getsize(dest) > 0:
                return href
    return None


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    seen = set()
    for e in entries('_data/media.yml'):
        outlet = e.get('outlet', '')
        if not outlet or outlet in seen:
            continue
        seen.add(outlet)
        name = slug(outlet, e.get('url', ''))
        if not name or outlet in NONE:
            print(f'first letter instead: {outlet}')
            continue
        dest = f'{OUT}/{name}.png'
        if os.path.exists(dest):
            continue
        site = SITE.get(outlet) or ('{0.scheme}://{0.netloc}'.format(urllib.parse.urlparse(e['url'])) if e.get('url') else None)
        if not site:
            print(f'no site, first letter instead: {outlet}')
            continue
        try:
            print(f'{outlet}: {logo(site, dest) or "none found"}')
        except Exception as err:
            print(f'{outlet}: failed ({err})')
