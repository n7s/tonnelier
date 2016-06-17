# Tonnelier

This is the Tonnelier fork of Cooper Hewitt.
Tonnelier is french for Cooper. 

Chester Jenkins of [Village](http://vllg.com/) created the custom typeface called Cooper Hewitt for the [Cooper Hewitt](http://www.cooperhewitt.org/) Smithsonian Design Museum.
(http://www.cooperhewitt.org/colophon/cooper-hewitt-the-typeface-by-chester-jenkins/).  
This design started life as Galaxie Polaris Condensed, a geometric, sans-serif font that Chester Jenkins had worked on years ago.
(https://vllg.com/constellation/galaxie-polaris-cond).

This Font Software is licensed under SIL Open Font License 1.1 (http://scripts.sil.org/OFL)  
See the FAQ on (http://scripts.sil.org/OFL-FAQ_web).

Cooper Hewitt is a trademark of Cooper Hewitt Smithsonian Design Museum.

See the [FONTLOG.txt](FONTLOG.txt) for all the details.

## Building the fonts with ufo2ft

Build dependencies:  
[Python](https://www.python.org/), [ufo2ft](https://github.com/jamesgk/ufo2ft),
[fonttools](https://github.com/behdad/fonttools), [ufoLib](https://github.com/unified-font-object/ufoLib), [Robofab](https://github.com/robofab-developers/robofab).

~~~
tools/build.py
~~~
(the files will show up in builds/)

## Building the fonts with smith

Build dependencies:  
[smith](https://github.com/silnrsi/smith)
~~~
smith configure
smith build
smith pdfs
smith zip
smith srcdist
smith exe 
smith distclean
~~~
(the files with show up in results/)
