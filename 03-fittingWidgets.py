from tkinter import *

root = Tk()

one = Label(root, text="One", bg="grey", fg="white")
one.pack()

two = Label(root, text="Two", bg="blue", fg="red")
two.pack(fill=X)

three = Label(root, text="Three", bg="white", fg="black")
three.pack(side=LEFT, fill=Y)

root.mainloop()
