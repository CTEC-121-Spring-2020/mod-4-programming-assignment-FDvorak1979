# Module 5
#   Programming Assignment 6
#       Prob-1.py

# Frank Dvorak

# INSTRUCTIONS:
#   Insert a comment above each line of code in the program below to describe
#   what the code does


from graphics import *

def main():
    # Creates the graphic window
     win = GraphWin("title", 1000, 1000)
    # Draws a cirlce within the graphic window at grid location 50, 50 and radious 20
     shape = Circle(Point(50,50), 20)
     # Sets the outline of the shape drawn to red.  Can RGB numbers be used?
     shape.setOutline("red")
     # Fills the shape with color
     shape.setFill("red")
     # Sets python for commands to be used for drawn shape
     shape.draw(win)
     # Sets the range for 5 movements or clicks of the  clircle
     for i in range(5):
         # Allows thwe window the capture mouse
          p = win.getMouse()
          # Calls up center point of circle
          c = shape.getCenter()

          # getws the x and y calues of center point and moves the circle in relation to mouse click
          dx = p.getX() - c.getX()
          dy = p.getY() - c.getY()
          # Allows the circle to be moved by mouse
          shape.move(dx,dy)
     win.close()

main()