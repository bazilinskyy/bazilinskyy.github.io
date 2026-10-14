# by Pavlo Bazilinskyy <pavlo.bazilinskyy@gmail.com>
# Builds _data/repos.json, the open-source cards at the end of the research page: my own
# GitHub repositories (not forks, not archived, with a description) plus EXTRA, most stars
# first, then most recently pushed. Run nightly by .github/workflows/nightly.yml; by hand:
#   python3 scripts/make_github.py
import json
import os
import urllib.request

USER = 'bazilinskyy'
EXTRA = ['crowd-dataset/crowd']  # repositories of mine under other accounts
SHOW = 8  # two rows of four cards
OUT = '_data/repos.json'


def get(path):
    req = urllib.request.Request(f'https://api.github.com/{path}', headers={'Accept': 'application/vnd.github+json'})
    if os.environ.get('GITHUB_TOKEN'):  # the Action's token: higher API rate limit
        req.add_header('Authorization', f"Bearer {os.environ['GITHUB_TOKEN']}")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def pick(repos):
    """The SHOW repositories to show, as small dicts, most stars first, then most recently pushed."""
    keep = [r for r in repos if not r['fork'] and not r['archived'] and r['description']]
    keep.sort(key=lambda r: r['pushed_at'], reverse=True)
    keep.sort(key=lambda r: r['stargazers_count'], reverse=True)  # stable: ties stay newest first
    return [dict(name=r['full_name'].removeprefix(f'{USER}/'), url=r['html_url'], description=r['description'],
                 language=r['language'], stars=r['stargazers_count'], forks=r['forks_count'], pushed=r['pushed_at'][:10])
            for r in keep[:SHOW]]


def _check():
    base = dict(fork=False, archived=False, description='d', language=None, forks_count=0, html_url='u')
    repos = [dict(base, full_name=f'{USER}/old', stargazers_count=1, pushed_at='2020-01-01T00:00:00Z'),
             dict(base, full_name=f'{USER}/new', stargazers_count=1, pushed_at='2026-01-01T00:00:00Z'),
             dict(base, full_name='org/top', stargazers_count=5, pushed_at='2021-01-01T00:00:00Z'),
             dict(base, full_name=f'{USER}/fork', stargazers_count=9, pushed_at='2026-01-01T00:00:00Z', fork=True),
             dict(base, full_name=f'{USER}/bare', stargazers_count=9, pushed_at='2026-01-01T00:00:00Z', description=None)]
    assert [r['name'] for r in pick(repos)] == ['org/top', 'new', 'old']


if __name__ == '__main__':
    _check()
    repos = get(f'users/{USER}/repos?per_page=100&type=owner') + [get(f'repos/{r}') for r in EXTRA]
    data = pick(repos)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"{OUT}: {', '.join(r['name'] for r in data)}")
