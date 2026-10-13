# by Pavlo Bazilinskyy <pavlo.bazilinskyy@gmail.com>
# Builds js/crowd-globe.json for the globe on the home page (and the totals in _data/crowd.json): the localities of the
# CROWD dataset (mapping.csv of github.com/crowd-dataset/crowd) with their hours of
# footage and the segments added in the last week and month. The mapping has
# no dates per segment, so "added" compares mapping.csv on main now with main as it
# was then (its commit history). A segment is a (video, start) pair, compared across
# all localities: their ids get renumbered.
# Run nightly by .github/workflows/crowd-globe.yml; by hand:
#   python3 scripts/make_crowd_globe.py
import csv
import io
import json
import os
import sys
import time
import urllib.request

REPO = 'crowd-dataset/crowd'
WEEK, MONTH = 7 * 86400, 30 * 86400  # seconds
OUT = 'js/crowd-globe.json'
TOTALS = '_data/crowd.json'  # the numbers in the text of the research page (site.data.crowd)


def get(url):
    req = urllib.request.Request(url)
    if os.environ.get('GITHUB_TOKEN'):  # the Action's token: higher API rate limit
        req.add_header('Authorization', f"Bearer {os.environ['GITHUB_TOKEN']}")
    return urllib.request.urlopen(req, timeout=120).read().decode()


def mapping(ago_s=0):
    """mapping.csv text on main as it was ago_s seconds ago ('' if the history does not go back that far)."""
    if not ago_s:
        return get(f'https://raw.githubusercontent.com/{REPO}/main/mapping.csv')
    until = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(time.time() - ago_s))
    commits = json.loads(get(f'https://api.github.com/repos/{REPO}/commits?sha=main&path=mapping.csv&until={until}&per_page=1'))
    return get(f"https://raw.githubusercontent.com/{REPO}/{commits[0]['sha']}/mapping.csv") if commits else ''


def segments(text):
    """{locality id: (lat, lon, name, hours, {(video, start), ...})} of a mapping.csv's text."""
    csv.field_size_limit(sys.maxsize)
    out = {}
    for row in csv.DictReader(io.StringIO(text)):
        try:
            lat, lon = float(row['lat']), float(row['lon'])
        except ValueError:
            continue
        videos = [v.strip() for v in row['videos'].strip('[]').split(',') if v.strip()]
        segs, hours = set(), 0.0
        for v, ss, es in zip(videos, json.loads(row['start_time'] or '[]'), json.loads(row['end_time'] or '[]')):
            for s, e in zip(ss, es):
                segs.add((v, s))
                hours += max(0, e - s) / 3600
        state = f", {row['state']}" if row.get('state') and row['country'] == 'United States' else ''
        out[row['id']] = (lat, lon, f"{row['locality']}{state}, {row['country']}", hours, segs)
    return out


def compare(now, week, month):
    """Points [lat, lon, hours, videos, segments new in a month, segments new in a week, name] and totals."""
    points, totals = [], dict(month=0, week=0, month_places=0, week_places=0)
    week, month = ({seg for v in old.values() for seg in v[4]} for old in (week, month))
    for lat, lon, name, hours, segs in now.values():
        m = len(segs - month) if month else 0
        w = len(segs - week) if week else 0
        totals['month'] += m
        totals['week'] += w
        totals['month_places'] += m > 0
        totals['week_places'] += w > 0
        points.append([round(lat, 2), round(lon, 2), round(hours, 1), len({v for v, _ in segs}), m, w, name])
    return points, totals


def _check():
    head = 'id,locality,state,country,lat,lon,videos,start_time,end_time\n'
    old = head + '1,Delft,,Netherlands,52.011,4.357,"[a,b]","[[0],[10,50]]","[[30],[20,60]]"\n2,Nowhere,,X,,,"[]","[]","[]"\n'
    new = old + '3,Gouda,,Netherlands,52.0,4.7,"[c]","[[0]]","[[3600]]"\n'
    new = new.replace('"[[0],[10,50]]","[[30],[20,60]]"', '"[[0],[10,50,70]]","[[30],[20,60,80]]"')
    pts, tot = compare(segments(new), segments(old), segments(old))
    assert {p[6]: (p[4], p[5]) for p in pts} == {'Delft, Netherlands': (1, 1), 'Gouda, Netherlands': (1, 1)}, pts
    assert tot == dict(month=2, week=2, month_places=2, week_places=2) and pts[0][:4] == [52.01, 4.36, 0.0, 2], (tot, pts)
    assert compare(segments(new), {}, {})[1]['month'] == 0  # no history: nothing is called new
    renumbered = old.replace('\n1,Delft', '\n9,Delft')
    assert compare(segments(old), segments(renumbered), {})[1]['week'] == 0  # same segments under a new id: not new


if __name__ == '__main__':
    _check()
    now, week, month = (segments(t) if t else {} for t in (mapping(), mapping(WEEK), mapping(MONTH)))
    points, totals = compare(now, week, month)
    data = dict(built=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), localities=len(points),
                countries=len({p[6].rsplit(', ', 1)[1] for p in points}), hours=round(sum(p[2] for p in points)),
                videos=len({v for *_, segs in now.values() for v, _ in segs}),
                **totals, points=points)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    with open(TOTALS, 'w', encoding='utf-8') as f:
        json.dump({k: data[k] for k in ('built', 'localities', 'countries', 'hours', 'videos')}, f, indent=2)
    print(f"{OUT}: {data['localities']} localities, {data['videos']} videos, {data['hours']} h, +{totals['week']} segments in a week, "
          f"+{totals['month']} in a month")
