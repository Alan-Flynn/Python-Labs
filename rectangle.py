# Name:        Your Name
# Student ID:  012345678

# File:        rectangle.py

############################################################################

import graphics

win = graphics.GraphWin("Click me")

prompt = graphics.Text(graphics.Point(100,100), "Click at two points")
prompt.draw(win)

p1 = win.getMouse()
p2 = win.getMouse()

rec = graphics.Rectangle(p1, p2)
rec.draw(win)

x1 = p1.getX()
y1 = p1.getY()
x2 = p2.getX()
y2 = p2.getY()

width = x2 - x1
heith = y2 - y1
perimeter = (abs(width) * 2) + (abs(heith) *2)
print("The permimeter is", perimeter, sep = ' ')

area = abs(width) * abs(heith)
print("The area is", area, sep =' ')

# this waits until you have clicked in the window to close it.
win.getMouse()
win.close()
