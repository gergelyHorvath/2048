import tkinter as tk
from tkinter import *
from tkinter import ttk

LARGE_FONT=("Verdana", 12)

def printing(*args):
            print("csa")



class Codecool2048 (tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column = 0, sticky="nsew")
        self.show_frame(StartPage)


    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        #gamesize
        Label (self, text="Game size:", fg="green", font="none 10 bold").grid(column=1, row=1)
        ttk.Button(self, text="3x3", command=print("asd3")).grid(column=1, row=2, sticky=W)
        ttk.Button(self, text="4x4", command=print("asd4")).grid(column=2, row=2, sticky=W)
        ttk.Button(self, text="5x5", command=print("asd5")).grid(column=1, row=3, sticky=W)
        ttk.Button(self, text="6x6", command=print("asd6")).grid(column=2, row=3, sticky=W)
        ttk.Button(self, text="7x7", command=print("asd7")).grid(column=1, row=4, sticky=W)
        ttk.Button(self, text="8x8", command=print("asd8")).grid(column=2, row=4, sticky=W)
        ttk.Button(self, text="9x9", command=print("asd9")).grid(column=1, row=5, sticky=W)
        ttk.Button(self, text="10x10", command=print("asd10")).grid(column=2, row=5, sticky=W)

        #Sizemanaging
        ttk.Label(self, text="  ", command=print("asd")).grid(column=3, row=1, sticky=W)
        ttk.Label(self, text="  ", command=print("asd")).grid(column=7, row=1, sticky=W)
        
        #diffbetweenobjects
        for child in self.winfo_children(): child.grid_configure(padx=5, pady=5)

        # Directons
        Label (self, text="Controls:", fg="green", font="none 10 bold").grid(column=5, row=5)
        ttk.Button(self, text="Up", command=printing).grid(column=5, row=4, sticky=W)
        ttk.Button(self, text="Down", command=print("asd")).grid(column=5, row=6, sticky=W)
        ttk.Button(self, text="Left", command=print("asd")).grid(column=4, row=5, sticky=W)
        ttk.Button(self, text="Right", command=print("asd")).grid(column=6, row=5, sticky=W)

        #Ai or Player
        Label (self, text="Mode:", fg="green", font="none 10 bold").grid(column=1, row=6)
        ttk.Button(self, text="AI mode", command=print("asd")).grid(column=1, row=7, sticky=W)
        ttk.Button(self, text="Player mode", command=print("asd")).grid(column=2, row=7, sticky=W)
        
        ttk.Button(self, text="Start game", command=print("asd")).grid(column=5, row=1, sticky=W)
        ttk.Button(self, text="End game", command=print("asd")).grid(column=6, row=1, sticky=W)
        
app= Codecool2048()
app.mainloop()