from tkinter import *
from tkinter import ttk

root = Tk()
root.wm_title("2048 Control Panel")
LARGE_FONT = ("Verdana", 9)
statusmsg = StringVar()
sentmsg = StringVar()

def statusbar(*args):
    idxs = sizes.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        showsize = gamesizes[idx]
        showmode = gamesizes[idx]
        statusmsg.set("Selected settings are size: %s , mode: %s" % (showsize, showmode))

#lists
gamesizes = ["3x3", "4x4, default", "5x5", "6x6", "7x7", "8x8", "9x9", "10x10"]
csizes = StringVar(value=gamesizes)


#gamesize
container = ttk.Frame(root, padding=(5, 5, 12, 0)) 
container.grid(column=0, row=1, sticky=(N,W,E,S))


sizes = Listbox(container, listvariable=csizes, height=8, width=14, bd=4)
sizes.grid(column=0, row=1, rowspan=6, sticky=(N,S,E,W))
sizes.selection_set(1)

lbl = ttk.Label(container, text="Map size", font=LARGE_FONT)
lbl.grid(column=0, row=0, padx=0, pady=5)

for i in range(0,len(gamesizes),2):
    sizes.itemconfigure(i, background='#f0f0ff')

#Ai or player
lbl = ttk.Label(container, text="Game mode", font=LARGE_FONT)
lbl.grid(column=2, row=0, padx=0, pady=5)
g1 = ttk.Radiobutton(container, text="normal Player mode", variable='gift', value='card')
g1.grid(column=2, row=2, sticky=W, padx=20)
g2 = ttk.Radiobutton(container, text="against AI", variable='gift', value='flowers')
g2.grid(column=2, row=3, sticky=W, padx=20)

#statusbar
sentlbl = ttk.Label(container, textvariable=sentmsg, anchor='center')
sentlbl.grid(column=3, row=5, columnspan=2, sticky=N, pady=5, padx=5)

#sendbutton
send = ttk.Button(container, text='Save & Play', command='sendGift', default='active')
send.grid(column=4, row=6, sticky='ES')

sizes.bind('<<ListboxSelect>>', statusbar)

#root.window min and max size
root.maxsize(500,500);
root.minsize(300,180);

sentmsg.set('')
statusmsg.set('gtreger')

root.mainloop()