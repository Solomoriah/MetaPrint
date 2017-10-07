#!/usr/bin/env python
# Setup for MetaPrint
# Modified from samples by Alex Martelli.

from distutils.core import setup

longdesc  =  """
MetaPrint.py defines a class and utility functions for use by programs 
which also use MSWinPrint.py for output.  MetaPrint exposes a document
class which replicates the functionality of MSWinPrint, but rather than
actually printing, a document object collects the output generated so
that it can be replayed, either via MSWinPrint or ImagePrint.  This is
useful mainly to preview a print job (by running the MetaPrint document
through ImagePrint) and subsequently actually print it (via MSWinPrint).

document is a class for creating and running print jobs.  Presently, the 
source is the only documentation for this class.

Development versions of this module may be found on **Github** at:

https://github.com/Solomoriah/MetaPrint
"""

setup(
    name = "MetaPrint",
    version = "1.0",
    description = "MetaPrint",
    long_description = longdesc,
    author = "Chris Gonnerman",
    author_email = "chris@gonnerman.org",
    py_modules = [ "MetaPrint" ],
    keywords = "windows printing",

    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Printing",
    ],
)

# end of file.
