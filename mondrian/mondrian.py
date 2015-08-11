#!/usr/bin/env python
'''
Create image like Mondrian drawings
'''

import sys
import random
 
try:
  import scribus
except ImportError,err:
	print "This Python script is written for the Scribus scripting interface."
	print "It can only be run from within Scribus."
	sys.exit(1)


def main(argv):

	rectColor = "Black"
	topMargin, leftMargin, rightMargin, bottomMargin = scribus.getPageMargins()
	pageWidth, pageHeight = scribus.getPageSize()
	printAreaWidth  = pageWidth  - leftMargin - rightMargin
	printAreaHeight = pageHeight - topMargin  - bottomMargin

	vertRectW = random.randrange(2,4)
	vertRectH = random.randrange(48,50)
	horRectW = random.randrange(47,49)
	horRectH = random.randrange(2,5)

	startx = leftMargin
	endx = pageWidth - leftMargin - horRectW
	starty = topMargin
	endy = pageHeight - topMargin - vertRectH

	numberRectVert = random.randrange(400,600)
	numberRectHor = random.randrange(400,600)
	opacity = 0

	scribus.progressTotal(numberRectVert+numberRectHor)
	scribus.setRedraw(False)

	for i in range(1, numberRectVert):
		opacity = opacity + 0.002
		xpos = random.randrange(int(startx),int(endx))
		ypos = random.randrange(int(starty),int(endy))
		rect = scribus.createRect(xpos, ypos, vertRectW, vertRectH)
		scribus.setFillColor(rectColor, rect)
		scribus.setLineColor("None", rect) 
		if opacity < 1:
			scribus.setFillTransparency(opacity, rect) 
		scribus.progressSet(i*2)


	for i in range(1, numberRectVert):
		opacity = opacity + 0.002
		xpos = random.randrange(int(startx),int(endx))
		ypos = random.randrange(int(starty),int(endy))
		recthor = scribus.createRect(xpos, ypos, horRectW, horRectH)
		scribus.setFillColor(rectColor, recthor)
		scribus.setLineColor("None", recthor) 
		if opacity < 1:
			scribus.setFillTransparency(opacity, recthor)

	scribus.progressReset()
	scribus.docChanged(True)
	scribus.statusMessage("Done")
	scribus.setRedraw(True)

def main_wrapper(argv):
  try:
		scribus.statusMessage("Running script...")
		scribus.progressReset()
		main(argv)
  finally:
		if scribus.haveDoc():
		    scribus.setRedraw(True)
		scribus.statusMessage("")
		scribus.progressReset()
 
if __name__ == '__main__':
    main_wrapper(sys.argv)

