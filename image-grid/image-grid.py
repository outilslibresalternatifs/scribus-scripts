#!/usr/bin/env python

"""Generate a grid of images from a directory.
Create a new doc. Ask user size of the doc, number of columns, lines and margins.
"""

""" Locale string (can be changed)""" 
docWidthStr1 = 'Paper Width'
docWidthStr2 = 'Enter the width of your document (in mm)'
docHeightStr1 = 'Document Height'
docHeightStr2 = 'Enter the height of your document (in mm)'
numColStr1 = 'Number of columns'
numColStr2 = 'Enter the number of columns of your grid? '
numLinStr1 = 'Number of Lines'
numLinStr2 = 'Enter the number of lines of your grid?'
gapStr1 = 'Margin Width'
gapStr2 = 'Enter the margins width of your grid (in mm)?'

""" Default Value in Dialog (can be changed) """
defaultDocWidth = '210'
defaultDocHeight = '297'
defaultNumColumns = '4'
defaultNumRows = '4'
defaultGap = '10'


import scribus
import os

filetype = []
dicttype = {'j':'.jpg','p':'.png','t':'.tif','g':'.gif','P':'.pdf'}
Dicttype = {'j':'.JPG','p':'.PNG','t':'.TIF','g':'.GIF','P':'.PDF'}
nrimages = '0'

# Ask which document size
docWidth = float(scribus.valueDialog(docWidthStr1,docWidthStr2,defaultDocWidth))
docHeight = float(scribus.valueDialog(docHeightStr1,docHeightStr2,defaultDocHeight))

# Generate grids
numColumns = int(scribus.valueDialog(numColStr1, numColStr2, defaultNumColumns))
numRows = int(scribus.valueDialog(numLinStr1, numLinStr2, defaultNumRows))
gap = float(scribus.valueDialog(gapStr1, gapStr2, defaultGap))
nbrimages = numColumns*numRows
imagedir = scribus.fileDialog('Select your pictures folder','Folders',isdir=True)
imagetype = scribus.valueDialog('Pictures types','Enter pictures types: j=jpg,p=png,t=tif,g=gif,P=pdf\n "jptgP" selects all','jptgP')
for t in imagetype[0:]:
    filetype.append(dicttype[t])
    filetype.append(Dicttype[t])
d = os.listdir(imagedir)
D = []
for file in d:
    for format in filetype:
        if file.endswith(format):
            D.append(file)
D.sort()

imagecount = 0

#framecount = 0
if len(D) > 0:
    # Create a new scribus document
    if scribus.newDoc((float(docWidth), float(docHeight)), (10,10,20,20),scribus.PORTRAIT, 1, scribus.UNIT_MILLIMETERS, scribus.FACINGPAGES, scribus.FIRSTPAGERIGHT):
        pageWidth, pageHeight = scribus.getPageSize()
        # The margins order is wrong in Scripter documentation
        topMargin, leftMargin, rightMargin, bottomMargin = scribus.getPageMargins()
        
        printAreaWidth  = pageWidth  - leftMargin - rightMargin
        printAreaHeight = pageHeight - topMargin  - bottomMargin 
        
        numVgaps = numColumns-1
        numHgaps = numRows-1
        columnWidth = (printAreaWidth-(numVgaps*gap)) / numColumns
        rowHeight = (printAreaHeight-(numHgaps*gap)) / numRows

        # Variables images
        imageWidth = columnWidth
        imageHeight = rowHeight
        xpos = []
        ypos = []

        xcount = leftMargin
        ycount = topMargin
        
				# Calculate position of images
        for i in range(1, numRows+1):
        	xcount = leftMargin
	        for i in range(1, numColumns+1):
	            xpos.append(xcount)
	            ypos.append(ycount)
	            xcount = xcount + columnWidth + gap

        	ycount = ycount + rowHeight + gap

        while imagecount < len(D):
            if imagecount > 0:
                scribus.newPage(-1)
                framecount = 0
# Here is where we're loading images into the page, four at a time, then go back up for a newPage
            for x,y in zip(xpos,ypos):
                if imagecount < len(D):
                    f = scribus.createImage(x, y, imageWidth, imageHeight)
                    scribus.loadImage(imagedir + '/' + D[imagecount], f)
                    scribus.setScaleImageToFrame(scaletoframe=1, proportional=1, name=f)
                    lenfilename = len(D[imagecount])
                    Lpiclen = int(5.3 * lenfilename)
                    imagecount += 1
    scribus.setRedraw(1)
    scribus.redrawAll()

else:
    result = scribus.messageBox ('Not Found','No Images found with\n this search selection',scribus.BUTTON_OK)
