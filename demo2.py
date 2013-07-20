#!/usr/bin/env python

'''

  Demo for the Hacktory's Lightbox (using the virtual lightbox
  object by default)

  Released into the public domain by Sharp Hall sharp@sauropod.org 2013

'''


from virtuallightbox import *

from time import sleep
from math import sin, cos

lb = Lightbox()

t = 0.0

while True:
    for x in range(0,lb.width):
        for y in range(0,lb.height):
            r = sin(t+sin(float(x)/5+t))*cos(t-sin(float(y)/3-t)) * 127 + 127
            g = cos(t+cos(float(x)/5+t))*sin(t-cos(float(y)/3-t)) * 127 + 127
            b  = cos(t+sin(float(x)/5+t))*sin(t-sin(float(y)/3-t)) * 127 + 127
            lb.set(x,y,Color(r,g,b))
    t += 0.08
    lb.flip()
    sleep(1.0/25)


