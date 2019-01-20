from tkinter import *

root = Tk()

# Labels
l1 = Label(root, text="Name")
l2 = Label(root, text="Password")

# Entries
e1 = Entry(root)
e2 = Entry(root)

# Checkbox
c = Checkbutton(root, text="Don't keep me logged in")

# Grid

# sticky= N,E,S,W
l1.grid(row=0, sticky=E)
l2.grid(row=1)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

c.grid(columnspan=2)

root.mainloop()
