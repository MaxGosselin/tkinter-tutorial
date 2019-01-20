from tkinter import *

import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title", "Men are from Mars.")

answer = tkinter.messagebox.askquestion("Q1", "What is the color of today?")

if answer == "yes":
    print("You are wise.")
else:
    print("That's absurd.")


root.mainloop()
