from tkinter import *


def leftClick(Event):
    print("Left")


def scrollwheelClick(Event):
    print("Middle")


def rightClick(Event):
    print("Right")


root = Tk()

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", scrollwheelClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root.mainloop()
