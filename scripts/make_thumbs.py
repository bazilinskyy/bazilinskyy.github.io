# Small copies of the publication images for the publications list and the sidebar, where they
# show about 110 px wide while the originals are 600 px or more: images/thumbs/<name>.jpg, 240 px
# wide (sharp on high-density screens). The pages fall back to the original where no thumbnail
# exists, and phones still get the original through srcset. Only images without a thumbnail are
# done (file times mean nothing after a git checkout); after replacing an image, run it with
# --all. Needs Pillow; runs nightly, or by hand:  python3 scripts/make_thumbs.py [--all]
import glob
import os
import sys

from PIL import Image

SRC = '_publications'
OUT = 'images/thumbs'
WIDTH = 240


def main():
    os.makedirs(OUT, exist_ok=True)
    made = 0
    for src in sorted(glob.glob(f'{SRC}/*.jpg') + glob.glob(f'{SRC}/*.png')):
        dest = f'{OUT}/{os.path.splitext(os.path.basename(src))[0]}.jpg'
        if os.path.exists(dest) and '--all' not in sys.argv:
            continue
        with Image.open(src) as im:
            im = im.convert('RGB')
            if im.width > WIDTH:
                im = im.resize((WIDTH, round(im.height * WIDTH / im.width)), Image.LANCZOS)
            im.save(dest, 'JPEG', quality=80, optimize=True, progressive=True)
        made += 1
    print(f'{made} thumbnails made')


if __name__ == '__main__':
    main()
