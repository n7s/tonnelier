#!/usr/bin/python3
# encoding: utf-8
# this is a smith configuration file

# set the default output folders for release docs
DOCDIR = ["documentation", "web"]

# set the font name, version, licensing and description
APPNAME = 'Tonnelier'
familyname = APPNAME

# Get VERSION and BUILDLABEL from Regular UFO; must be first function call:
getufoinfo('source/' + familyname + '-Regular' + '.ufo')


DESC_SHORT = "A fork of Cooper Hewitt with reorganized repository and buildpath"

for style in ('Regular', 'Book', 'BookItalic', 'Medium', 'MediumItalic', 'Heavy', 'HeavyItalic', 'Light', 'LightItalic', 'Bold', 'BoldItalic', 'Semibold', 'SemiboldItalic', 'Thin', 'ThinItalic' ) :
	font(target = APPNAME + '-' + style + '.ttf',
	source = 'source/' + APPNAME + '-' + style + '.ufo',
	version = VERSION,
	opentype = internal(),
	script = ['latn'],
	fret = fret(params = '-r'),
	)
