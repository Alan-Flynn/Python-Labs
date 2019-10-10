# Name:        Your Name
# Student ID:  012345678

# File:        ngon.py

############################################################################

import graphics         # Note that the file graphics.py must be
                                # in the same directory as this file
import math

def draw_points(win, n, p, r):
    x = p.getX()
    y = p.getY()
    for i in range(n):
        x1 = x + r*math.cos(i*2*math.pi/n)
        y1 = y + r*math.sin(i*2*math.pi/n)
        graphics.Point(x1, y1).draw(win)
        


