from tkinter import *


def exFunc(Event):
    print("This is an example!")


root = Tk()

# first way
# b1 = Button(root, text="What is this?", command=exFunc)
# b1.pack()

# Event

b1 = Button(root, text="What is this?")
b1.bind("<Button-1>", exFunc)
b1.pack()

root.mainloop()
