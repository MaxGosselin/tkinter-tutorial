from tkinter import *


def doNothing():
    print("Fine then...")


root = Tk()

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


root.mainloop()
