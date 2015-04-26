
#!/usr/bin/env python

# This simple script will produce a progress-bar style pagination
# on the pages of your existing Scribus document.
# Created by Raphael Bastide for outilslibresalternatifs.org
# https://github.com/outilslibresalternatifs/scribus-scripts

from scribus import *

# The page thumbnails color, must be set in the document's color palette
barColor = "Black"
# The bar height. Document's unit
barHeight = 100
pageWidth = getPageSize()[0]
pageHeight = getPageSize()[1]
pageWidthMargin = getPageMargins()[1] + getPageMargins()[2]
pageBottomLimit = pageHeight - getPageMargins()[0] - barHeight
pageInnerWidth = pageWidth - pageWidthMargin
xPos = getPageMargins()[1]
yPos = pageBottomLimit
pageNumber = pageCount()
barWidthUnit = pageInnerWidth / pageNumber
currentPage = 1

while (currentPage <= pageNumber):
    barWidth = barWidthUnit * currentPage
    gotoPage(currentPage)
    rect = createRect(xPos, yPos, barWidth, barHeight)
    setFillColor(barColor, rect)
    currentPage += 1
