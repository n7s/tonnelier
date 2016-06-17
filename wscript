#!/usr/bin/python
# encoding: utf-8
# this is a smith configuration file

# set the default output folders
out="results"
DOCDIR="documentation"
OUTDIR="installers"
ZIPDIR="releases"
TESTDIR='tests'
TESTRESULTSDIR = 'tests'
STANDARDS = 'tests/reference'

# set the version control system
#VCS='git'

# set the font name, version, licensing and description
APPNAME = 'Tonnelier'
VERSION = '2.000'
TTF_VERSION='2.000'
COPYRIGHT="Copyright (c) 2016, Cooper Hewitt (http://www.cooperhewitt.org) with Reserved Font Name 'Cooper Hewitt'"
LICENSE = 'OFL.txt'

DESC_SHORT = "A fork of Cooper Hewitt with reorganized repository and buildpath"
DESC_LONG = """This fork of Cooper Hewitt provide ufo-to-otf-ttf buildpath as part of a reorganized repository
Font sources are published in the repository and a ufo2ft and smith open workflow is used for building, testing and releasing.
"""

# packaging
DESC_NAME = "Tonnelier"
DEBPKG = 'fonts-tonnelier'


# script information
finfo = {
	"Example.txt" : "script=DFLT",
	"Example-roman.txt" : "script=latn"
	}

for style in ('Regular', 'Book', 'BookItalic', 'Medium', 'MediumItalic', 'Heavy', 'HeavyItalic', 'Light', 'LightItalic', 'Bold', 'BoldItalic', 'Semibold', 'SemiboldItalic', 'Thin', 'ThinItalic' ) :
	font(target = APPNAME + '-' + style + '.ttf',
	source = 'source/' + APPNAME + '-' + style + '.ufo',
	version = VERSION,
	opentype = internal(),
	script = ['latn'],
	fret = fret(params = '-r'),
	)
