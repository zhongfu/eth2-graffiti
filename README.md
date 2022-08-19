# eth2-graffiti

*because i'm bad with names*

this helps you draw graffiti on the beaconcha.in graffitiwall with your 
lighthouse validator... or something

## Usage

- make your images: one per stage, e.g. outlines, then with fill, then with
  translucent pixels, then with background
  - should be RGBA images, e.g. png with alpha channel
  - any pixels not at 100% opacity will be ignored
- put your image(s) somewhere
- stick all your validator pubkeys into `validators.txt`, one per line
- copy `settings.py.example` to `settings.py` and edit it

- run `main.py` every now and then, so put it in a cronjob or something
  - maybe don't run it too often though because it pulls existing pixels
    on the graffitiwall from beaconcha.in
- point lighthouse to the `graffiti.txt` that `main.py` writes

## Requirements

idk, `pillow` maybe? `requests`?

eth2 validators too? lol
