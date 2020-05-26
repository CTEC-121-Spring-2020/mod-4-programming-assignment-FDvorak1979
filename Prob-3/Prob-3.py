# Module 5
#   Programming Assignment 6
#       Prob-3.py

# Frank Dvorak
from graphics import *

def main():
    win = GraphWin("title", 1000, 1000)
    shape1 = Circle(Point(500,500), 500)
    shape1.setFill("Black")
    shape1.draw(win)
    shape2 = Circle(Point(500,500), 400)
    shape2.setFill("Blue")
    shape2.draw(win)
    shape3 = Circle(Point(500,500), 300)
    shape3.setFill("yellow")
    shape3.draw(win)
    shape4 = Circle(Point(500,500), 150)
    shape4.setFill("red")
    shape4.draw(win)
    input()
    
main()    