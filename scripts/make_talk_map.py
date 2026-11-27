# Builds _data/talk_map.json for the map on the talks page: every place where I gave a talk or
# chaired, with its coordinates and the talks there. Run nightly by .github/workflows/nightly.yml;
# by hand:
#   python3 scripts/make_talk_map.py
# Places come from
# - _data/conference_talks.yml and _data/chairing_sessions.yml: the end of "conf", e.g.
#   "... (AutoUI), Seoul, South Korea."
# - _data/chairing_autoui.yml, _data/chairing_roman.yml and any entry with "location:", which
#   overrides the above; invited talks appear once they have one
# Online talks are left out. Coordinates come from OpenStreetMap Nominatim, asked only for places
# the previous file does not have yet (at most one request a second, as its policy asks).
import json
import os
import re
import time
import urllib.parse
import urllib.request

OUT = '_data/talk_map.json'
SOURCES = [  # file, kind shown in the popup
    ('_data/invited_talks.yml', 'Invited talk'),
    ('_data/conference_talks.yml', 'Conference talk'),
    ('_data/chairing_sessions.yml', 'Session chair'),
    ('_data/chairing_autoui.yml', 'AutoUI'),
    ('_data/chairing_roman.yml', 'RO-MAN'),
]


def entries(path):
    """The list of flat 'key: value' records in a data file (the site's YAML files are that simple)."""
    out, cur = [], None
    for line in open(path, encoding='utf-8'):
        m = re.match(r'^(-\s+|\s+)([a-z_]+):\s*(.*?)\s*$', line)
        if not m:
            continue
        if m.group(1).startswith('-'):
            cur = {}
            out.append(cur)
        value = m.group(3)
        if len(value) > 1 and value[0] == value[-1] and value[0] in '"\'':
            value = value[1:-1].replace('\\"', '"')
        cur[m.group(2)] = value
    return out


def place_of(entry):
    """'City, Country' of a talk, or None when it was online or names no place."""
    text = entry.get('location') or entry.get('conf') or ''
    if 'online' in text.lower() or 'hybrid' in text.lower():
        return None
    text = text.strip().rstrip('.').strip()
    if not entry.get('location'):
        # after the venue's acronym "(X)," or "(X).", else after the first comma
        m = re.search(r'\)[.,]\s*([^()]+)$', text)
        text = m.group(1) if m else (text.split(', ', 1)[1] if ', ' in text else '')
    return text.strip() or None


def geocode(place):
    url = 'https://nominatim.openstreetmap.org/search?' + urllib.parse.urlencode(dict(q=place, format='json', limit=1))
    req = urllib.request.Request(url, headers={'User-Agent': 'static-site-talk-map/1.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        hits = json.load(r)
    time.sleep(1.1)
    return (round(float(hits[0]['lat']), 4), round(float(hits[0]['lon']), 4)) if hits else None


def build(known):
    places = {}
    for path, kind in SOURCES:
        if not os.path.exists(path):
            continue
        for e in entries(path):
            place = place_of(e)
            if place:
                places.setdefault(place, []).append(dict(title=e.get('title', ''), kind=kind, year=int(e.get('year') or 0)))
    out = []
    for place, talks in places.items():
        coords = known.get(place) or geocode(place)
        if not coords:
            print(f'not found, left off the map: {place}')
            continue
        out.append(dict(place=place, lat=coords[0], lon=coords[1],
                        talks=sorted(talks, key=lambda t: (-t['year'], t['title']))))
    return sorted(out, key=lambda p: (-len(p['talks']), p['place']))


def _check():
    assert place_of({'conf': 'International ACM Conference on (AutoUI), Brisbane, QLD, Australia.'}) == 'Brisbane, QLD, Australia'
    assert place_of({'conf': 'Conference (IHIET-AI). Valencia, Spain'}) == 'Valencia, Spain'
    assert place_of({'conf': 'Car.HMI, Berlin, Germany'}) == 'Berlin, Germany'
    assert place_of({'conf': 'SMC, Toronto, Canada (online)'}) is None
    assert place_of({'conf': 'x', 'location': 'Gothenburg, Sweden'}) == 'Gothenburg, Sweden'
    assert place_of({'title': 'no place'}) is None


if __name__ == '__main__':
    _check()
    known = {}
    if os.path.exists(OUT):
        known = {p['place']: (p['lat'], p['lon']) for p in json.load(open(OUT, encoding='utf-8'))}
    data = build(known)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'talk map: {len(data)} places, {sum(len(p["talks"]) for p in data)} talks')
