# Module 5
#   Programming Assignment 6
#       Prob-2.py

# Frank Dvorak

from graphics import *

def main():
     win = GraphWin("prob-2", 1000, 1000)
     shape = Rectangle(Point(50,50), Point(100,100))
     shape.setOutline("red")
     shape.draw(win)
for i in range(5):
     # Allows thwe window the capture mouse
     p = win.getMouse()
     # Calls up center point of circle
     c = shape.getCenter()

     # getws the x and y calues of center point and moves the circle in relation to mouse click
     dx = p.getX() - c.getX()
     dy = p.getY() - c.getY()
     # Allows the circle to be moved by mouse
     shape.clone(dx,dy)
     
main()