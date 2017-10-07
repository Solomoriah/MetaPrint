# MetaPrint.py
# Copyright (c) 2008-2017 Chris Gonnerman
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions
# are met:
# 
# Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer. 
# 
# Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution. 
# 
# Neither the name of the author nor the names of any contributors
# may be used to endorse or promote products derived from this software
# without specific prior written permission. 
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
MetaPrint.py defines a class and utility functions for use by programs 
which also use MSWinPrint.py for output.  MetaPrint exposes a document
class which replicates the functionality of MSWinPrint, but rather than
actually printing, a document object collects the output generated so
that it can be replayed, either via MSWinPrint or ImagePrint.  This is
useful mainly to preview a print job (by running the MetaPrint document
through ImagePrint) and subsequently actually print it (via MSWinPrint).

document is a class for creating and running print jobs.  Presently, the 
source is the only documentation for this class.
"""

class document:

    def __init__(self, desc = None, printer = None, 
            papersize = "letter", orientation = "portrait", duplex = "normal"):
        self.font = None
        self.printer = printer
        self.papersize = papersize
        self.orientation = orientation
        self.duplex = duplex
        self.page = 0
        self.pagelist = []
        self.pagedata = []
        if desc is not None:
            self.desc = desc
        else:
            self.desc = "MetaPrint.py print job"

    def begin_document(self, desc = None):
        if desc:
            self.desc = desc

    def end_document(self):
        if self.pagedata:
            self.end_page()

    def end_page(self):
        if self.pagedata:
            self.pagelist.append(self.pagedata)
        self.pagedata = []
        if self.font is not None:
            self.pagedata.append(self.font)

    def line(self, from_, to):
        self.pagedata.append(("line", (from_, to)))

    def rectangle(self, box):
        self.pagedata.append(("rectangle", box))

    def text(self, position, text):
        self.pagedata.append(("text", (position, text)))

    def setfont(self, name, size, bold = None, italic = 0):
        self.font = ("font", (name, size, bold, italic))
        self.pagedata.append(self.font)

    def image(self, position, image, size):
        self.pagedata.append(("image", (position, image, size)))

    def setink(self, ink):
        self.pagedata.append(("setink", (ink,)))

    def setfill(self, onoff):
        self.pagedata.append(("setfill", (onoff,)))

    def runpage(self, doc, page):
        for op, args in page:
            if op == "line":
                doc.line(*args)
            elif op == "rectangle":
                doc.rectangle(args)
            elif op == "text":
                doc.text(*args)
            elif op == "font":
                doc.setfont(*args)
            elif op == "image":
                doc.image(*args)
            elif op == "setink":
                doc.setink(*args)
            elif op == "setfill":
                doc.setfill(*args)
        doc.end_page()
        
    def run(self, doc, pageno = None):
        if pageno is None:
            for page in self.pagelist:
                self.runpage(doc, page)
        else:
            self.runpage(doc, self.pagelist[pageno])

# end of file.
