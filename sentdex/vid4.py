import tkinter as tk

LARGE_FONT = ("Arial", 12)


class demoApp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):

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
        label = tk.Label(self, text="ehhhhh lmao", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        b1 = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
        b1.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NO lmao", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        b1 = tk.Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
        b1.pack()

app = demoApp()
app.mainloop()
