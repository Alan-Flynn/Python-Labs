# Name:        Your Name
# Student ID:  012345678

# File:        archery.py

############################################################################
import graphics

win = graphics.GraphWin()

center1 = graphics.Point(100,100)
circle1 = graphics.Circle(center1, 15)
circle1.setFill('yellow')

center2 = graphics.Point(100,100)
circle2 = graphics.Circle(center2, 30)
circle2.setFill('red')

center3 = graphics.Point(100,100)
circle3 = graphics.Circle(center3, 45)
circle3.setFill('blue')

center4 = graphics.Point(100,100)
circle4 = graphics.Circle(center4, 60)
circle4.setFill('black')

center5 = graphics.Point(100,100)
circle5 = graphics.Circle(center5, 75)
circle5.setFill('white')

circle5.draw(win)
circle4.draw(win)
circle3.draw(win)
circle2.draw(win)
circle1.draw(win)


# this waits until you have clicked in the window to close it.
win.getMouse()
win.close()
