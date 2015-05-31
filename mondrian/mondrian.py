#!/usr/bin/env python
'''
Create image like Mondrian drawings
'''

import scribus
import random

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

for i in range(1, numberRectVert):
	opacity = opacity + 0.002
	xpos = random.randrange(int(startx),int(endx))
	ypos = random.randrange(int(starty),int(endy))
	rect = scribus.createRect(xpos, ypos, vertRectW, vertRectH)
	scribus.setFillColor(rectColor, rect)
	scribus.setLineColor("None", rect) 
	if opacity < 1:
		scribus.setFillTransparency(opacity, rect) 


for i in range(1, numberRectVert):
	opacity = opacity + 0.002
	xpos = random.randrange(int(startx),int(endx))
	ypos = random.randrange(int(starty),int(endy))
	recthor = scribus.createRect(xpos, ypos, horRectW, horRectH)
	scribus.setFillColor(rectColor, recthor)
	scribus.setLineColor("None", recthor) 
	if opacity < 1:
		scribus.setFillTransparency(opacity, recthor) 