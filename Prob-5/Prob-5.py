# Module 5
#   Programming Assignment 6
#       Prob-5.py

# Frank Dvorak

from graphics import *



def main():
    win = GraphWin("Prob-5.py", 800, 800) 
    
    body = Rectangle(Point(500,400), Point(100,600))
    body.setFill("green")
    body.draw(win)

    tire = Circle(Point(180, 600), 50)
    tire.setFill("black")
    tire.draw(win)
    hubcap = Circle(Point(180, 600), 30)
    hubcap.setFill("gray")
    hubcap.draw(win)

    cab = Rectangle(Point(650, 450), Point(500,600))
    cab.setFill("green")
    cab.draw(win)

    winshield = Rectangle(Point(650, 465), Point(560,550))
    winshield.setFill("black")
    winshield.draw(win)

    fbumper = Rectangle(Point(655, 590), Point(590,570))
    fbumper.setFill("gray")
    fbumper.draw(win)

    tire2 = Circle(Point(510, 600), 50)
    tire2.setFill("black")
    tire2.draw(win)
    hubcap2 = Circle(Point(510, 600), 30)
    hubcap2.setFill("gray")
    hubcap2.draw(win)

    rbumper = Rectangle(Point(90, 590), Point(120, 570))
    rbumper.setFill("gray")
    rbumper.draw(win)
    input() 

main()