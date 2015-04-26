
#!/usr/bin/env python

# This simple script will produce a progress-bar style pagination
# on the pages of your existing Scribus document.
# Created by Raphael Bastide for outilslibresalternatifs.org
# https://github.com/outilslibresalternatifs/scribus-scripts

from scribus import *

barColor = "Black"
barHeight = 100
pageNumber = pageCount()
pageWidth = getPageSize()[0]
pageHeight = getPageSize()[1]
pageWidthMargin = getPageMargins()[1] + getPageMargins()[2]
pageBottomLimit = pageHeight - getPageMargins()[0] - barHeight
pageInnerWidth = pageWidth - pageWidthMargin
barWidthUnit = pageInnerWidth / pageNumber
xPos = getPageMargins()[1]
yPos = pageBottomLimit
currentPage = 1

while (currentPage <= pageNumber):
    barWidth = barWidthUnit * currentPage
    gotoPage(currentPage)
    print barWidth
    rect = createRect(xPos, yPos, barWidth, barHeight)
    setFillColor(barColor, rect)
    currentPage += 1
