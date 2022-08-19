#!/usr/bin/env python3
from PIL import Image

from beaconchain import get_graffitiwall_pixels
from imgutil import *
from settings import IMG_ORIGIN, IMG_STAGES, GRAFFITI_SHORT, GRAFFITI_DEFAULT

stages = list(Image.open(file) for file in IMG_STAGES)
sizes = set(img.size for img in stages)
assert len(sizes) == 1, "no stages configured, or some stages have different sizes!"
img_size = sizes.pop()

bounds = (
    IMG_ORIGIN[0],
    IMG_ORIGIN[0] + img_size[0],
    IMG_ORIGIN[1],
    IMG_ORIGIN[1] + img_size[1],
)

assert len(GRAFFITI_SHORT.encode('utf-8')) <= 16, "short graffiti is too long"
assert len(GRAFFITI_DEFAULT.encode('utf-8')) <= 32, "default graffiti is too long"
assert all(0 <= x < 1000 for x in bounds), "image is outside of graffitiwall bounds"

def write_graffiti(lines: list[str]):
    with open('graffiti.txt', 'w') as f:
        if not lines:
            f.write(f'default: {GRAFFITI_DEFAULT}\n')
        else:
            f.writelines(l + '\n' for l in lines)

def main():
    with open('validators.txt', 'r') as f:
        validators = f.read().strip().split()

    graffitiwall_pixlist = get_graffitiwall_pixels(bounds)

    lines = None

    for img in stages:
        img_pixlist = get_pixels(img, IMG_ORIGIN)

        cur_diff = pixlist_diff(img_pixlist, graffitiwall_pixlist)

        if len(cur_diff) == 0:
            continue

        lines = assign_pixlist_to_validators(cur_diff, validators, GRAFFITI_SHORT)
        break

    write_graffiti(lines)

if __name__ == '__main__':
    main()
