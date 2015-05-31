#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys
 
try:
    import scribus
except ImportError,err:
    print "This Python script is written for the Scribus scripting interface."
    print "It can only be run from within Scribus."
    messageBox(TITLE, "erreur", ICON_INFORMATION)
    sys.exit(1)

TITLE = 'Text gradient'
# errors
error_message_main_error = "An unknown error happened while calling main()."
error_message_colours_undefined = "Either or both 'start' and 'stop' colours are undefined. Please define them the Edition->Colours Menu)"
error_message_selection_error = "An unknown error happened while calling getSelection()."
error_message_gradient_simple = "An unknown error happened while calling simpleGradient()."
error_message_gradientpoint = "An unknown error happened while calling gradientPoint(). Returned a dummy value (0)."
error_message_CMYKgradientpoint = "An unknown error happened while calling CMYKgradientPoint(). Returned a dummy value (0, 0, 0, 0)."
error_message_sequential_selection = "An unknown error happened while calling sequentialTextFrameSelection()."
error_message_apply_gradient = "An unknown error happened while calling sequentialTextFrameSelection()."

# success
success_message = "sequential_text_gradient was successfully applied."

def main():
    """
    This script applies a colour gradient to all the characters, sequentially,
    of all the selected TextFrame objects in Scribus.
    You have to define two colours (start and stop) prior to run it.
    """
    try:
        # first, get the colors
        CMYKstart, CMYKend = getColors()
        # second, the selection of item we can actually work on
        selection = getSelection()
        # If the values are not defined or if there is no selection, 
        # we stop here, if they are, we continue
        if CMYKstart != None and CMYKend != None and len(selection)>0:
            sequentialTextFrameSelection(selection, CMYKstart, CMYKend, simpleGradient)
            print success_message
            scribus.messageBox(TITLE, success_message, scribus.ICON_INFORMATION)
    except:
        print error_message_main_error
        scribus.messageBox(TITLE, error_message_main_error, scribus.ICON_WARNING)
        if debug != None:
            scribus.messageBox(TITLE, debug, scribus.ICON_WARNING)


def getColors():
    '''Get the stop and start color from Scribus environment.
    (This implies that you must define two colours names start and stop prior to launch this.'''
    start = None
    stop = None
    try: 
        return scribus.getColor('start'), scribus.getColor('stop')
    except:
        print error_message_colours_undefined
        scribus.messageBox(TITLE, error_message_colours_undefined, scribus.ICON_WARNING)
        return None, None

def getSelection():
    '''Returns a list of the selected TextFrame objects.
    Returns an empty list if there is no TextFrame Object currently selected.'''
    try:
        filtered_selection = [] # list we're going to use to put all the TextFrame elements
        # first, we check if there is something to work on
        if scribus.selectionCount() > 0:
            # then we check for each element
            # if it's a TextFrame object.
            # if so, we add it's name to the filtered list.
            for i in range (0,scribus.selectionCount()):
                if scribus.getObjectType(scribus.getSelectedObject(i)) == 'TextFrame':
                    filtered_selection.append(scribus.getSelectedObject(i))
        return filtered_selection
    except:
        print error_message_selection_error
        scribus.messageBox(TITLE, error_message_selection_error, scribus.ICON_WARNING)
        return []

def CMYKgradientPoint(CMYKstart,CMYKend,steps,currentStep):
    '''Returns CMYK values based on the given parameters.
    CMYKstart, CMYKend : tuple of size 4.
    As strange as it is, Scribus encode CMYK values from 0 to 255.'''
    try:
        C = int(round(gradientPoint(CMYKstart[0],CMYKend[0],steps,currentStep)))
        M = int(round(gradientPoint(CMYKstart[1],CMYKend[1],steps,currentStep)))
        Y = int(round(gradientPoint(CMYKstart[2],CMYKend[2],steps,currentStep)))
        K = int(round(gradientPoint(CMYKstart[3],CMYKend[3],steps,currentStep)))
        return (C,M,Y,K)
    except:
        print error_message_CMYKgradientpoint
        scribus.messageBox(TITLE, error_message_CMYKgradientpoint, scribus.ICON_WARNING)
        return (0, 0, 0, 0)

def gradientPoint(start,stop,steps,currentStep):
    '''return the value of a point at step currentStep/steps
    on a gradient between start and stop.'''
    try:
        return start + currentStep * ( stop - start ) / (steps - 1.0)
    except:
        print error_message_gradientpoint
        scribus.messageBox(TITLE, error_message_gradientpoint, scribus.ICON_WARNING)
        return 0

def applyGradient(gradient_function,gradient_parameters):
    '''Run the given gradient function with the given parameters.'''
    try:
        gradient_function(gradient_parameters)
    except:
        print error_message_apply_gradient
        scribus.messageBox(TITLE, error_message_apply_gradient, scribus.ICON_WARNING)

def sequentialTextFrameSelection(selection, CMYKstart, CMYKend, gradient_function):
    '''Run the given function sequentially on each element of the selection list argument.'''
    try:
        for TextFrame_object in selection:
            applyGradient(gradient_function,(TextFrame_object,CMYKstart,CMYKend))
    except:
        print error_message_sequential_selection
        scribus.messageBox(TITLE, error_message_sequential_selection, scribus.ICON_WARNING)

def simpleGradient(my_parameters):
    '''Applies a simple (character by character) gradient to a TextFrame object'''
    try:
        TextFrame_object = my_parameters[0]
        CMYKstart = my_parameters[1]
        CMYKend = my_parameters[2]
        object_length = scribus.getTextLength(TextFrame_object)
        for i in range(0,object_length):
            scribus.selectText(i, 1, TextFrame_object)
            color = CMYKgradientPoint(CMYKstart,CMYKend,object_length,i)
            try:
                getColor(str(color))
            except:
                scribus.defineColor(str(color), color[0], color[1], color[2], color[3])
            scribus.setTextColor(str(color), TextFrame_object)
    except:
        print error_message_gradient_simple
        scribus.messageBox(TITLE, error_message_gradient_simple, scribus.ICON_WARNING)

main()