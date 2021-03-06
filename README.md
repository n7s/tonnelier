# Tonnelier

This is the Tonnelier fork of Cooper Hewitt.  
Tonnelier is french for Cooper. 


[![Build Status](https://travis-ci.org/n7s/tonnelier.svg?branch=master)](https://travis-ci.org/n7s/tonnelier)

Chester Jenkins of [Village](http://vllg.com/) created the [custom typeface called Cooper Hewitt](http://www.cooperhewitt.org/colophon/cooper-hewitt-the-typeface-by-chester-jenkins/) for the [Cooper Hewitt](http://www.cooperhewitt.org/) Smithsonian Design Museum.  
This design started life as [Galaxie Polaris Condensed](https://vllg.com/constellation/galaxie-polaris-cond) a geometric, sans-serif font that Chester Jenkins had worked on years ago.

This Font Software is licensed under SIL Open Font License 1.1 [(scripts.sil.org/OFL)](http://scripts.sil.org/OFL)  
See the FAQ on [scripts.sil.org/OFL-FAQ_web](http://scripts.sil.org/OFL-FAQ_web).

Cooper Hewitt is a trademark of Cooper Hewitt Smithsonian Design Museum.

See the [FONTLOG.txt](FONTLOG.txt) for all the details.

## Building the fonts with ufo2ft

Build dependencies: [Python](https://www.python.org/), [ufo2ft](https://github.com/jamesgk/ufo2ft), 
[fonttools](https://github.com/behdad/fonttools), [ufoLib](https://github.com/unified-font-object/ufoLib), [Robofab](https://github.com/robofab-developers/robofab).

~~~
tools/build.py
~~~
(the font files will show up in builds/)

## Building the fonts with smith

Build dependencies:  [smith](https://github.com/silnrsi/smith)
~~~
smith configure
smith build
smith pdfs
smith zip
smith srcdist
smith distclean
~~~
(the various files with show up in results/)


## Generating specimens

Dependencies: [sile](http://sile-typesetter.org/)  
(the fonts must have been built obviously)
~~~
sile documentation/specimen.sil
~~~
