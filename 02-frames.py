from tkinter import *

# Main window
root = Tk()

# Frames
topFrame = Frame(root)
topFrame.pack()
botFrame = Frame(root)
botFrame.pack(side=BOTTOM)

# Widgets
button1 = Button(topFrame, text="Don't click me.", fg="red")
button2 = Button(topFrame, text="Don't click me.", fg="green")
button3 = Button(topFrame, text="Don't click me.", fg="blue")
button4 = Button(botFrame, text="CLICK ME!", fg="magenta")

# Pack widgets
# reminder: when packing, by default things are stacked vertically)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

root.mainloop()

