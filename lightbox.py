'''

 This module defines the Hacktory's Lightbox.
 Different types of Lightboxes (virtual, real) inherit
 these classes.

 (c) 2013 Sharp Hall sharp@sauropod.org GPLv3

'''

class Color:
    r = 0
    g = 0
    b = 0
    
    def __init__(self, red, green, blue):
        red = int(red)
        green = int(green)
        blue = int(blue)
        if red < 0: red = 0
        elif red > 255: red = 255
        if green < 0: green = 0
        elif green > 255: green = 255
        if blue < 0: blue = 0
        elif blue > 255: blue = 255
        self.r = red
        self.g = green
        self.b = blue
    
    def __repr__(self):
        return("<Color, red: " + str(self.r) + ", green: "
               + str(self.g) + ", blue: " + str(self.b) + ">")

class Lightbox:

    def __init__(self, height = 10, width = 16,
                 fillcolor = Color(0,0,0)):
        self.width = width
        self.height = height
        self.fillcolor = fillcolor
        self.pixels = [ [ fillcolor for y in range(self.height) ]
                   for x in range(self.width) ]
        self.init_screen()

    def init_screen(self):
        pass

    def __repr__(self):
        return "<Hacktory Lightbox!>"
    
    def set(self,x,y,c):
        if x >= self.width or y >= self.height: return False
        if x < 0 or y < 0: return False
        self.pixels[x][y] = c
        self.hwset(x,y)
        return True
        
    def hwset(self,x,y):
        c = self.pixels[x][y]
        self.ser.write(bytearray([width*y+x+1, c.r, c.g, c.b]))
    
    def flip(self):
        pass

    def get(self,x,y):
        return self.pixels[x][y]
    
    def blit_pygame_surface(self,surface,left = 0,top = 0,width = None,
                            height = None, startx = 0, starty = 0):
        swidth = surface.get_width()
        sheight = surface.get_height()
        
        if width == None: width = swidth
        if height == None: height = sheight

        for y in xrange(starty,height):
            for x in xrange(startx,width):
                if y >= sheight or x >= swidth:
                    self.set(x + left, y + top, self.fillcolor)
                else:
                    color = surface.get_at((x,y))
                    color = Color(color.r, color.g, color.b)
                    self.set(x + left, y + top, color)

                
