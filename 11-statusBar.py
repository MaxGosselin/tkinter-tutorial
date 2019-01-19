from tkinter import *


def doNothing():
    print("Fine then...")


root = Tk()

# **** MAIN MENU ****

# Add a menu
menu = Menu(root)
root.config(menu=menu)

# Create sub menus and append them to the main menu.
subMenu = Menu(menu)
sub2Menu = Menu(menu)


menu.add_cascade(label="Example", menu=subMenu)
menu.add_cascade(label="2", menu=sub2Menu)

# Add to the cascading submenu
subMenu.add_command(label="Do Nothing", command=doNothing)
subMenu.add_command(label="Again", command=doNothing)
subMenu.add_command(label="Last Time", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Quit", command=root.quit)

# **** TOOLBAR ****

toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="Insert", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
inertButt = Button(toolbar, text="Print", command=doNothing)
inertButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# **** STATUS BAR ****

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
