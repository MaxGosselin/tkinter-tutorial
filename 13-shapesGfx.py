from tkinter import *

import tkinter.messagebox

root = Tk()

# Make canvas
canvas = Canvas(root, width=500, height=500)
canvas.pack()

# Draw some shapes

# Lines are black by default
blackline = canvas.create_line(10, 10, 490, 490)
redline = canvas.create_line(10, 490, 490, 10, fill="red")

# Rectangle params are : (x1, y1, x2, y2)
# where (x1, y1) is the position of the top left corner
# and (x2, y2) is the bottom right.
greenBox = canvas.create_rectangle(175, 175, 350, 350, fill="green")

root.mainloop()
