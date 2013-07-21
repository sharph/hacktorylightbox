#!/usr/bin/env python

'''
  Demo for the Hacktory's Lightbox (using the virtual lightbox
  object by default)

  Released into the public domain by Sharp Hall sharp@sauropod.org 2013

'''

import pygame
import time
import requests
import random

from virtuallightbox import *
from math import sin, cos

lb = Lightbox()

text = "The Hacktory"
lasttemptime = 0
tempstring = ""

pygame.font.init()

font = pygame.font.Font(pygame.font.match_font('bitstreamverasans'),
                        lb.height)

def get_temp():
    p = {'q': 'Philadelphia,PA,USA'}
    r = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params=p, timeout=1.0)
    return r.json()['main']['temp'] * 9.0/5.0 - 459.67 # deg K to deg F

def scroll_surface(lb,surface,top):
    for left in xrange(lb.width, 0-surface.get_width()-1, -1):
        lb.blit_pygame_surface(surface, left, -2, surface.get_width()+1)
        lb.flip()
        time.sleep(1.0/10)

while True:
    try:
        if lasttemptime + 5 * 60 < time.time():
            lasttemptime = time.time()
            tempstring = str(int(get_temp())) + u'\u00b0'
    except Exception:
        tempstring = ""
    
    timestring = time.strftime("%I:%M")
    if timestring[0] == '0': timestring = timestring[1:]
    
    finaltext = text + "  " + timestring + "  " + tempstring
    
    r = [ random.randint(0,255), 0, 255 ]
    random.shuffle(r)
    rendered = font.render(finaltext, True,
                           pygame.Color(r[0],r[1],r[2],255),
                           pygame.Color(0,0,0,255))
    
    scroll_surface(lb,rendered,-2)

