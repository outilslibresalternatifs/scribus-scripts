#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import wikipedia article to scribus page
# Bachir Soussi Chiadmi - 2015 - outilslibresalternatifs.org - ola#0


import sys
sys.path.append('/usr/lib/python3.4/site-packages')

import random
import string
import wikipedia
import scribus

# help(string)


# CONSTANTS
# nbr_pages = 4
bpX, bpY = scribus.getPosition('wiki')
bW, bH = scribus.getSize('wiki')

# block_txt_w = (bW)/2
block_txt_w = 50
nbr_col = bW / block_txt_w


# INIT
def init():
  # k = 0
  c = 0
  y = bpY
  x = bpX
  h = 0

  full = 0
  # for i in xrange(0,nbr_pages):
  while full == 0 :
    cont = getRandWikiPage()

    y = y+h

    h = h+ newWikiTextBlock(cont,x,y,block_txt_w)

    if h+5 > bH :
      c = c+1
      y = bpY
      x = bpX+(block_txt_w + 5)*c
      h = 0
      if x + block_txt_w > bpX + bW:
        full = 1
    else :
      y = y+5


# scribus.deleteObject('wiki')


# random string
def randomWord(length):
  return ''.join(random.sample(string.ascii_lowercase,length))

# function to get a wikipedia page (handling ambigious query)
def getWikiPage(title):
  try:
    page = wikipedia.page(title)
  except wikipedia.exceptions.DisambiguationError as e:
    print(e.options)
    title = random.choice(e.options)
    page = wikipedia.page(title)
  return page

def getRandWikiPage():
  c = {}
  # set wikipedia to the good language and run a search for the string
  wikipedia.set_lang('fr')
  # get a random string
  randw = randomWord(3)
  # search
  search = wikipedia.search(randw)
  # randomly choose a result
  title = random.choice(search)
  # get the page for this result
  c["wp"] = getWikiPage(title)
  # ny.title, ny.url,, ny.content, ny.images[0], ny.links[0]

  c["summary"] = wikipedia.summary(title)

  return c
# nbr_pages = scribus.valueDialog("Pages", "combien de pages souhaitez-vous importer?")
#if scribus.newDoc(scribus.PAPER_LETTER, (10,10,20,20),scribus.PORTRAIT, 1, scribus.UNIT_POINTS, scribus.NOFACINGPAGES, scribus.FIRSTPAGERIGHT):

def newWikiTextBlock(cont,x,y,w):
  h = 0
  #title
  title = scribus.createText(x, y, w, 1)
  scribus.setText(cont["wp"].title, title)
  scribus.setTextAlignment(scribus.ALIGN_LEFT, title)
  scribus.setFont("Open Sans Bold", title)
  scribus.setFontSize(14, title)
  scribus.setLineSpacing(14, title)

  tw,th = scribus.getSize(title)
  while scribus.textOverflows(title):
    scribus.sizeObject(tw, th+1, title)
    tw,th = scribus.getSize(title)

  h = th

  #content
  content = scribus.createText(x, y+h+1, w, 1)
  scribus.setText(cont["summary"], content)
  scribus.setTextAlignment(scribus.ALIGN_LEFT, content)
  scribus.setFont("Open Sans Regular", content)
  scribus.setFontSize(10, content)

  tw,th = scribus.getSize(content)
  while scribus.textOverflows(content):
    scribus.sizeObject(tw, th+1, content)
    tw,th = scribus.getSize(content)
    if h+th > bH:
      break

  h = h+th

  return h

#run
init()