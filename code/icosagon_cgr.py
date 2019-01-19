#/usr/bin/python3.7
""" icosagon_cgr.py
Author: Kevin Dick
Date: 2019-01-16
---
Creates an Icosagonal Chaos Game Representation 
of a given amino acid sequence.
"""
import mapping_module as mm
from PIL import Image

RADIUS = 500

icodict = mm.create_icosagon_dict(RADIUS)
print(icodict)

# Create a Blank Image with Dimensions (2r, 2r)
img = Image.new('RGBA', (2*RADIUS, 2*RADIUS), color=255)
img.show()
for px in img:
    print(img.getpixel(px))
