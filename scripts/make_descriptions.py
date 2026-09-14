# by Pavlo Bazilinskyy <pavlo.bazilinskyy@gmail.com>
import argparse
import glob
import json
import os
import re
import sys

import yaml

# jekyll-seo-tag reads page.description, falling back to page.excerpt and then
# to site.description. These documents have no body, so without a description
# every page would share the generic site description. The value is derived
# from the abstract, so edit the abstract and re-run this: anything written by
# hand into description: will be overwritten.
COLLECTIONS = ['_publications/*.md', '_workshops/*.md']
MAX_CHARS = 160
FRONT_MATTER = re.compile(r'^---\n(.*?)\n---(\n.*)?$', re.DOTALL)


def shorten(text, max_chars=MAX_CHARS):
    """Cut text to a meta description of at most max_chars, on a word boundary.

    Args:
        text (string): Full abstract.
        max_chars (int): Longest description to produce, ellipsis included.

    Returns:
        string: Single-line description.
    """
    text = re.sub(r'\s+', ' ', text).strip()
    if len(text) <= max_chars:
        return text
    # one character of the budget belongs to the ellipsis
    cut = text[:max_chars - 1]
    if ' ' in cut:
        cut = cut[:cut.rfind(' ')]
    return cut.rstrip(' ,;:.') + '…'


def describe(path, quiet=False):
    """Give one document a description derived from its abstract.

    Args:
        path (string): Markdown file with Jekyll front matter.

    Returns:
        bool: True if the file was rewritten.
    """
    text = open(path, encoding='utf-8').read()
    match = FRONT_MATTER.match(text)
    if not match:
        print('Skipping %s: no front matter.' % path)
        return False
    front, body = match.group(1), match.group(2) or '\n'
    fields = yaml.safe_load(front) or {}
    if not fields.get('abstract'):
        return False
    wanted = shorten(fields['abstract'])
    if fields.get('description') == wanted:
        return False
    # rewrite line by line rather than dumping the parsed YAML, so quoting and
    # key order elsewhere in the front matter are left untouched
    lines = [ln for ln in front.split('\n')
             if not ln.startswith('description:')]
    after_title = next(i for i, ln in enumerate(lines)
                       if ln.startswith('title:'))
    # json.dumps, not yaml.safe_dump: dumping a bare scalar appends a "..."
    # document-end marker, and JSON string syntax is valid YAML double quoting
    lines.insert(after_title + 1,
                 'description: ' + json.dumps(wanted, ensure_ascii=False))
    with open(path, 'w', encoding='utf-8') as f:
        f.write('---\n' + '\n'.join(lines) + '\n---' + body)
    if not quiet:
        print('Described %s.' % os.path.basename(path))
    return True


def selftest():
    """Check the only part with any logic in it."""
    assert shorten('short one') == 'short one'
    assert shorten('a b', 2) == 'a…'
    long = 'word ' * 100
    assert len(shorten(long)) <= MAX_CHARS
    assert shorten(long).endswith('…')
    assert not shorten(long).endswith(' …'), 'trailing space before cut'
    assert shorten('one two three.', 12) == 'one two…', shorten('one two three.', 12)
    assert shorten('  spaced \n  out  ') == 'spaced out', 'whitespace not collapsed'
    print('selftest ok')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Derive description: from abstract: for SEO metadata.')
    parser.add_argument('--selftest', action='store_true',
                        help='check shorten() and exit')
    parser.add_argument('--print-changed', action='store_true',
                        help='print only the paths rewritten, for the git hook')
    args = parser.parse_args()
    if args.selftest:
        selftest()
        sys.exit(0)
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    changed = [p
               for pattern in COLLECTIONS
               for p in sorted(glob.glob(os.path.join(root, pattern)))
               if describe(p, quiet=args.print_changed)]
    if args.print_changed:
        if changed:
            print('\n'.join(changed))
    else:
        print('%d file(s) updated.' % len(changed))
