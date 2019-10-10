# Name:        Your Name
# Student ID:  012345678

# File:        pattern.py

############################################################################

import graphics

win = graphics.GraphWin()
j = 19
for i in range (5, 200, 10):    
    for j in range (5, 200, 10):
        p = graphics.Point(i, j)
        circle = graphics.Circle(p, 4)
        circle.setFill('green')
        circle.draw(win)

# this waits until you have clicked in the window to close it.
win.getMouse()
win.close()
