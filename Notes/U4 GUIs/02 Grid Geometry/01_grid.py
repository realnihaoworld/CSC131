from tkinter import *

window = Tk()

l1 = Label(window, text="A Label")
l1.grid(row=0, column=0, sticky=E)

l2 = Label(window, text="Another Label")
l2.grid(row=1, column=0, sticky=E)

e1 = Entry(window)
e1.grid(row=0, column=1)

e2 = Entry(window)
e2.grid(row=1, column=1)

window.mainloop()