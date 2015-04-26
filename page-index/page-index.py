#!/usr/bin/env python

# This simple script will produce a graphic page index
# of your document on the selected page
# Created by Raphael Bastide for outilslibresalternatifs.org
# https://github.com/outilslibresalternatifs/scribus-scripts

from scribus import *

pageNumber = pageCount()
currentPage = 1

# Scale factor of the page thumbnails, 1 is the real page size
factor = 0.1
# The page thumbnails color, must be set in the document's color palette
pageColor = "Black"
pageWidth = getPageSize()[0]
pageHeight = getPageSize()[1]
pageWidthMargin = getPageMargins()[1] + getPageMargins()[2]
pageInnerWidth = pageWidth - pageWidthMargin
xPos = getPageMargins()[1]
yPos = getPageMargins()[0]
gutter = 10
nextX = xPos
nextY = yPos
maxH = 0

while (currentPage <= pageNumber):
    lastPage = currentPage - 1
    pageSize = getPageNSize(currentPage)
    thumbWidth =  pageSize[0] * factor
    thumbHeight = pageSize[1] * factor
    if nextX + thumbWidth >= pageInnerWidth:
        nextY = nextY + maxH + gutter
        nextX = xPos
        maxH = 0
        pass
    if lastPage == 0 and maxH == 0:
        rect = createRect(nextX, nextY, thumbWidth, thumbHeight)
        setFillColor(pageColor, rect)
        nextX = nextX + thumbWidth + gutter
        maxH = thumbHeight
        pass
    else:
        lastPageW = getPageNSize(lastPage)[0] * factor
        lastPageH = getPageNSize(lastPage)[1] * factor
        rect = createRect(nextX, nextY, thumbWidth, thumbHeight)
        setFillColor(pageColor, rect)
        nextX = nextX + thumbWidth + gutter
        if thumbHeight > maxH:
            maxH = thumbHeight
            pass
    currentPage += 1
