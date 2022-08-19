import json
import requests

from settings import GRAFFITIWALL_URL

def get_graffitiwall_pixels(bounds: tuple[int, int, int, int] = (0, 0, 1000, 1000)):
    """
    bounds: [ax, ay, bx, by] (width [ax, bx[, height [ay, by[)
    returns: list of [x, y, rgb-hex]
    """
    ax, ay, bx, by = bounds

    resp = requests.get(GRAFFITIWALL_URL)
    assert resp.status_code == 200, "invalid http status code"

    lines = list(filter(lambda x: 'var pixels =' in x, resp.text.split('\n')))
    assert len(lines) == 1, "graffitiwall format is weird"

    jsondata = lines[0].split('=', 1)[1]
    jsonpixels = json.loads(jsondata)

    pixels = []

    for pix in jsonpixels:
        x = pix['x']
        y = pix['y']
        if ax <= x < bx and ay <= y < by:
            pixels.append([x, y, pix['color']])

    return pixels

