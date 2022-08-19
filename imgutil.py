import math
import random
from PIL import Image

def get_pixels(img: Image, offset: tuple[int, int]):
    """
    returns a list of [x, y, rgb-hex]
    but only for pixels where the alpha channel val is 255
    """
    assert img.mode == 'RGBA', "mode must be RGBA"

    ox, oy = offset

    w, h = img.size
    pixels = []

    data = img.getdata()

    for x in range(0, w):
        for y in range(0, h):
            pix = data[y * w + x]
            if pix[3] == 255:
                pixhex = '{:02x}{:02x}{:02x}'.format(*pix[0:3])
                pixels.append([ox + x, oy + y, pixhex])

    return pixels


def pixlist_to_array(size: tuple[int, int], pixlist: list[tuple[int, int, str]]):
    arr = list(list(None for i in range(0, size[1])) for i in range(0, size[0]))

    for pix in pixlist:
        arr[pix[0]][pix[1]] = pix[2]

    return arr


def pixlist_diff(desired: list[tuple[int, int, str]], actual: list[tuple[int, int, str]], actual_size: tuple[int, int] = (1000, 1000)):
    """
    returns a list of [x, y, rgb-hex]
    """
    diff = []

    src = pixlist_to_array(actual_size, actual)

    for pix in desired:
        x, y, col = pix
        if src[x][y] != col:
            diff.append(pix)

    return diff


def assign_pixlist_to_validators(pixlist: list[tuple[int, int, str]], validators: list[str], vanity: str = None):
    """
    returns list of strings; each string represents one line to be written to lighthouse graffiti.txt
    """
    pixels = random.choices(pixlist, k=len(validators) + 1)
    lines = []

    assert len(vanity) <= 16, "vanity len must be <= 16char"

    for i in range(0, len(validators)):
        x, y, col = pixels[i]
        val = validators[i]
        if vanity:
            lines.append(f'{val}: gw:{x:03d}{y:03d}{col} {vanity}')
        else:
            lines.append(f'{val}: gw:{x:03d}{y:03d}{col}')

    i += 1
    x, y, col = pixels[i]
    if vanity:
        lines.append(f'default: gw:{x:03d}{y:03d}{col} {vanity}')
    else:
        lines.append(f'default: gw:{x:03d}{y:03d}{col}')

    return lines
