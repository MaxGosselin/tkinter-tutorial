import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animu
from matplotlib import style

import tkinter as tk
from tkinter import ttk


LARGE_FONT = ("Arial", 12)
style.use("ggplot")

class demoApp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="icon.ico")
        tk.Tk.wm_title(self, "Telfer is coming.")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, GraphPage):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


def qf(param):
    print(param)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="ehhhhh lmao", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        b1 = ttk.Button(
            self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne)
        )
        b1.pack()

        b2 = ttk.Button(
            self, text="Visit Graph Page", command=lambda: controller.show_frame(GraphPage)
        )
        b2.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="NO lmao", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        b1 = ttk.Button(
            self, text="Home", command=lambda: controller.show_frame(StartPage)
        )
        b1.pack()

class GraphPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="mpl", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        b1 = ttk.Button(
            self, text="Home", command=lambda: controller.show_frame(StartPage)
        )
        b1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[81,76,69,58,44,32,20,5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

app = demoApp()
app.mainloop()
