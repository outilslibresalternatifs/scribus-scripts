
#!/usr/bin/env python

import scribus
import sys
import os
from random import randint
magtxt = 'Enter a magnetude number between 1 and 10'
pagetxt = 'What page to shake?'
magnetude = int(scribus.valueDialog("Magnetude",magtxt,"1"))
page = int(scribus.valueDialog("Enter page number, '0' for all",pagetxt,"1"))
pagenum = scribus.pageCount()
content = []
if page == 0:
	page = 1
else:
	pagenum = page
	pass
while (page <= pagenum):
	scribus.gotoPage(page)
	d = scribus.getPageItems()
	for item in d:
		rand = randint(- magnetude * 10 , magnetude * 10)
		itemname = item[0]
		print itemname
		scribus.rotateObjectAbs(rand,itemname)
		scribus.moveObject(rand,rand,itemname)
	page += 1
