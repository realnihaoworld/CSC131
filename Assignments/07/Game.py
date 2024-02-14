from tkinter import *
from CardGame import *

window = Tk()

window.title("CSC131 Card Game")
window.geometry('1000x1000')

l1 = Label(window, text="Computer picked")
l1.grid(row=0, column=0, sticky=W, ipadx=20)

l2 = Label(window, text="You picked")
l2.grid(row=0, column=4, sticky=E, ipadx=20)

window.columnconfigure(4, weight=1)
window.mainloop()