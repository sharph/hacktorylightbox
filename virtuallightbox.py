'''

  This module defines a virtual lightbox using pygame that can
  be used to test programs before being output on the real
  lightbox.

  (c) 2013 Sharp Hall sharp@sauropod.org GPLv3

'''


import lightbox
import pygame

class Color(lightbox.Color):
    pass

class Lightbox(lightbox.Lightbox):
    
    def init_screen(self):
        pygame.display.init()
        pygame.display.set_caption("Virtual Hacktory Lightbox")
        self.pgscreen = pygame.display.set_mode([self.width*30,
                                                 self.height*30])
        self.pgscreen.fill(pygame.Color(0,0,0,255))

    def hwset(self,x,y):
        rect = pygame.Rect(x*30,y*30,30,30)
        c = self.pixels[x][y]
        self.pgscreen.fill(pygame.Color(c.r, c.g, c.b, 255),rect=rect)
    
    def flip(self):
        pygame.display.flip()

