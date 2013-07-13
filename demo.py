
'''

  Demo for the Hacktory's Lightbox (using the virtual lightbox
  object by default)

  Released into the public domain by Sharp Hall sharp@sauropod.org 2013

'''


from virtuallightbox import *

from random import randint
from time import sleep

lb = Lightbox()

while True:
    c = Color(randint(0,255),randint(0,255),randint(0,255))
    lb.set(randint(0,lb.width-1),randint(0,lb.height-1),c)
    lb.flip()
    sleep(0.1)


