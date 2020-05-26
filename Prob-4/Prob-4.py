# Module 5
#   Programming Assignment 6
#       Prob-4.py

# Frank Dvorak

from graphics import *

def main():
# Sets up the Window
    win = GraphWin("Prob-4.py",500,500)

# Draws the frame of the house
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    frame = Rectangle(p1, p2)
    frame.draw(win)

# Draws the Door of the house
    p3 = win.getMouse()
    widthOfhouse = p2.y - p1.y
    doorWidth = widthOfhouse / 5
    halfDoorwidth = doorWidth / 2
    door = Rectangle(Point(p3.x - halfDoorwidth, p1.y), Point(p3.x + halfDoorwidth, p3.y))
    door.draw(win)

# Draws Window
    p4 = win.getMouse()
    windowWidth = widthOfhouse / 3
    halfWindowwidth = windowWidth / 2
    window = Rectangle(Point(p4.x - halfWindowwidth, p4.y + halfWindowwidth), Point(p4.x + halfWindowwidth, p4.y - halfWindowwidth))
    window.draw(win)

# Draws Roof
    p5 = win.getMouse()
    roofs1 = Line(p5, p2)
    roofs1.draw(win)
    roofs2 = Line(p5, Point(p1.x, p2.y))
    roofs2.draw(win)

    input()

main()