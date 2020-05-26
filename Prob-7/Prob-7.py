# Module 5
#   Programming Assignment 6
#       Prob-7.py

# Frank Dvorak

from graphics import *

def main():
# Sets window
    win = GraphWin("Prob-7.py", 800, 800)

# draws face structure    
    faceshape = Circle(Point(400, 400), 150)
    faceshape.setFill("olive")
    faceshape.draw(win)

# draws hat
    hat = Polygon(Point(150, 350), Point(400, 150), Point(650, 350))
    hat.setFill("black")
    hat.draw(win)

# draws eye balls
    leftEyeball = Circle(Point(320, 390), 40)
    leftEyeball.setFill("white")
    leftEyeball.draw(win)

    rightEyeball = Circle(Point(480, 390), 40)
    rightEyeball.setFill("white")
    rightEyeball.draw(win)

# Draws Iris
    leftIris = Circle(Point(320, 390), 25)
    leftIris.setFill("red")
    leftIris.draw(win)

    rightIris = Circle(Point(480, 390), 25)
    rightIris.setFill("red")
    rightIris.draw(win)

# Draws Puples
    leftPuple = Circle(Point(320, 390), 12)
    leftPuple.setFill("black")
    leftPuple.draw(win)

    rightPuple = Circle(Point(480, 390), 12)
    rightPuple.setFill("black")
    rightPuple.draw(win)

# Draws Mouth

    mouth = Line(Point(310, 465), Point(490, 465))
    mouth.draw(win)





    input()

main()