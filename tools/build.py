#!/usr/bin/python

from ufo2ft import compileTTF
from robofab.world import OpenFont

family = "Tonnelier"
weights = ["Regular", "Thin", "ThinItalic", "Light", "LightItalic", "Book", "BookItalic", "Medium", "MediumItalic", "Semibold", "SemiboldItalic", "Bold", "BoldItalic", "Heavy", "HeavyItalic"]

for w in weights:
    ufo = OpenFont("source/{}-{}.ufo".format(family, w))
    ttf = compileTTF(ufo, preProcessorClass=<class 'ufo2ft.preProcessor.TTFPreProcessor'>, outlineCompilerClass=<class 'ufo2ft.outlineCompiler.OutlineTTFCompiler'>, featureCompilerClass=<class 'ufo2ft.featureCompiler.FeatureCompiler'>, kernWriterClass=None, markWriterClass=None, featureWriters=None, glyphOrder=None, useProductionNames=None, convertCubics=True, cubicConversionError=None, reverseDirection=True, removeOverlaps=False, inplace=False),

    print ("Building " + "builds/{}-{}.ttf".format(family, w) + " from source file " + "source/{}-{}.ufo".format(family, w) + "...")
    ttf.save("builds/{}-{}.ttf".format(family, w))

print ("Done.")
