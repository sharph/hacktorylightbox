#!/usr/bin/env python

'''
  Demo for the Hacktory's Lightbox (using the virtual lightbox
  object by default)

  Released into the public domain by Sharp Hall sharp@sauropod.org 2013

'''

import pygame
import time
import requests

from virtuallightbox import *
from math import sin, cos

lb = Lightbox()

lasttemp = 0
text = "The Hacktory"
tempstring = ""

pygame.font.init()

font = pygame.font.Font(pygame.font.match_font('bitstreamverasans'),
                        lb.height)

def get_temp():
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Philadelphia,PA,USA")
    return r.json()['main']['temp'] * 9.0/5.0 - 459.67

def scroll_surface(lb,surface,top):
    for left in range(lb.width, 0-surface.get_width()-1, -1):
        lb.blit_pygame_surface(surface, left, -2, surface.get_width()+1)
        lb.flip()
        time.sleep(1.0/10)

while True:
    if lasttemp + 5 * 60 < time.time():
        lasttemp = time.time()
        tempstring = str(int(get_temp())) + u'\u00b0'
    
    timestring = time.strftime("%I:%M")
    if timestring[0] == '0': timestring = timestring[1:len(timestring)]
    
    finaltext = text + "  " + timestring + "  " + tempstring    
    rendered = font.render(finaltext, True, pygame.Color(255,255,255,255),
                           pygame.Color(0,0,0,255))
    
    scroll_surface(lb,rendered,-2)

