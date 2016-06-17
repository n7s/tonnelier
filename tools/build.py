#!/usr/bin/python
#
# you need
# https://github.com/jamesgk/ufo2ft
# https://github.com/behdad/fonttools
# https://github.com/unified-font-object/ufoLib
# https://github.com/robofab-developers/robofab


from ufo2ft import compileOTF
from robofab.world import OpenFont
import sys
import os

family = "Tonnelier"
weights = ["Regular", "Thin", "ThinItalic", "Light", "LightItalic", "Book", "BookItalic", "Medium", "MediumItalic", "Semibold", "SemiboldItalic", "Bold", "BoldItalic", "Heavy", "HeavyItalic"]

for w in weights:
    ufo = OpenFont("source/{}-{}.ufo".format(family, w))
    otf = compileOTF(ufo, useProductionNames=True, mtiFeaFiles=None, glyphOrder=None, optimizeCff=True)
    print ("Building " + "builds/{}-{}.otf".format(family, w) + " from source file " + "source/{}-{}.ufo".format(family, w) + "...")
    otf.save("builds/{}-{}.otf".format(family, w))

print ("Done.")


