#!/usr/bin/env python
'''
Add gradient background to every pages of the document'''

import scribus
import random

topMargin, leftMargin, rightMargin, bottomMargin = scribus.getPageMargins()
pageWidth, pageHeight = scribus.getPageSize()
printAreaWidth  = pageWidth  - leftMargin - rightMargin
printAreaHeight = pageHeight - topMargin  - bottomMargin

xPos = 0
yPos = 0

pageNumber = scribus.pageCount()
currentPage = 1
scribus.createLayer("background")

while (currentPage <= pageNumber):
    scribus.gotoPage(currentPage)
    c = random.randint(0,150)
    m = random.randint(0,150)
    y = random.randint(0,150)
    k = random.randint(0,150)
    gradientType = random.randint(1,5)
    scribus.defineColor("color1", c, m, y, k) 
    scribus.defineColor("color2", k, y, m, c) 
    rect = scribus.createRect(xPos, yPos, pageWidth, pageHeight)
    scribus.setGradientFill(gradientType, "color1", 90, "color2", 90, rect)
    #scribus.setGradientFill(1, "Black", 90, "White", 90, rect)
    currentPage += 1