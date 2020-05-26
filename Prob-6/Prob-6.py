# Module 5
#   Programming Assignment 6
#       Prob-6.py

# <YOUR NAME>

from graphics import *

def main():
    win = GraphWin("Prob-6.py", 800,800)

# Draws Lego 1
    block1 = Rectangle(Point(50, 50,), Point(190, 100))
    block1.draw(win)

    niba1 = Rectangle(Point(65, 45), Point(50, 50))
    niba1.draw(win)

    niba2 = Rectangle(Point(70, 45), Point(85, 50))
    niba2.draw(win)
    
    niba3 = Rectangle(Point(90, 45), Point(105, 50))
    niba3.draw(win)

    niba4 = Rectangle(Point(125, 45), Point(110, 50))
    niba4.draw(win)

    niba5 = Rectangle(Point(145, 45), Point(130, 50))
    niba5.draw(win)

    niba6 = Rectangle(Point(130, 45), Point(145, 50))
    niba6.draw(win)

    niba7 = Rectangle(Point(165, 45), Point(150, 50))
    niba7.draw(win)

    niba8 = Rectangle(Point(190, 45), Point(170, 50))
    niba8.draw(win)

# Draws Lego 2
    block2 = Rectangle(Point(50, 160), Point(190, 130))
    block2.draw(win)
    
    nibb1 = Rectangle(Point(65, 130), Point(50, 200))
    nibb1.draw(win)

    nibb2 = Rectangle(Point(70, 45), Point(85, 130))
    nibb2.draw(win)
    
    nibb3 = Rectangle(Point(90, 45), Point(105, 30))
    nibb3.draw(win)

    nibb4 = Rectangle(Point(125, 45), Point(110, 50))
    nibb4.draw(win)

    nibb5 = Rectangle(Point(145, 45), Point(130, 50))
    nibb5.draw(win)

    nibb6 = Rectangle(Point(130, 45), Point(145, 50))
    nibb6.draw(win)

    nibb7 = Rectangle(Point(165, 45), Point(150, 50))
    nibb7.draw(win)

    nibb8 = Rectangle(Point(190, 45), Point(170, 50))
    nibb8.draw(win)
    input()

main()