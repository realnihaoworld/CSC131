from tkinter import *


label1_style = {
    'bg': 'red', 
    'fg': 'white'
}

label2_style = {
    'bg': 'green', 
    'fg': 'white'
}

label3_style = {
    'bg': 'blue', 
    'fg': 'white'
}

window = Tk()

# bg is for background
# fg is for textcolor

# ** unpacks dictionary as arguments (kwargs)
l1 = Label(window, text="A", **label1_style)
l1.pack(side=LEFT, fill=X, expand=1)

l2 = Label(window, text="B", **label2_style)
l2.pack(side=LEFT, fill=BOTH, expand=1)

l3 = Label(window, text="C", **label3_style)
l3.pack(side=LEFT, expand=1, fill=X)

window.mainloop()

