# Module 5
#   Programming Assignment 6
#       Prob-5.py

# Frank Dvorak

import tkinter
root=tkinter.Tk()
root.title("Draw a Car")
c=tkinter.Canvas(root, width=1200, height=500)
c.grid(row=0, column=0)

#rearwheel
c.create_oval(300,300,400,400, fill="black")
c.create_oval(320,320,380,380, fill="grey")

#frontwheel
c.create_oval(600,300,700,400, fill="black")
c.create_oval(620,320,680,380, fill="grey")

#bottonlines
c.create_line(400,350,600,350, width=3)
c.create_line(700,350,900,350, width=3)
c.create_line(50,350,300,350, width=3)

#rear
c.create_line(100,250,50,350, width=3)

#front
c.create_line(900,250,1000,300,900,350, width=3, smooth="true")

#top
c.create_line(350,150,500,100,650,150, width=3, smooth="true")

#middleline
c.create_line(100,250,900,250, width=3)

#horizontal_middle/rear/front
c.create_line(500,125,500,250, width=3)
c.create_line(350,150,350,250, width=3)
c.create_line(650,150,650,250, width=3)

#rearwindow
c.create_line(100,250,200,250,350,150, width=3)

#windshield
c.create_line(650,150,800,250,850,250, width=3, smooth="true")


root.mainloop()