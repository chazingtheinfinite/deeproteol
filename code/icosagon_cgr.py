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
img = Image.new('RGBA', (2*RADIUS, 2*RADIUS), color=(255, 255,255,255))

#for i in range(img.size[0]): # for every pixel:
#    for j in range(img.size[1]):
#        print(f'{(i,j)} : {img.getpixel((i,j))}')

# TODO:: Create definition for setting a patch around the pixel to make obvious points...

pixels = img.load()
for aa in icodict.keys():
    i,j = icodict[aa]
    print(f'Setting black to {(i,j)}: {aa}')
    pixels[i-1,j-1] = (0,0,0,255)


img.show()
