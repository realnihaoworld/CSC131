from tkinter import *
# import tkinter as tk

# create object reference for the window
window = Tk()

# create a label widget
# attach it to the window
text = Label(window, text="This is my GUI")

# must manage the geometry of the element to get it to appear
# one way is with pack()
text.pack()

window.mainloop()