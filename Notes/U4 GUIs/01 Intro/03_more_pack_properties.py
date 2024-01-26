from tkinter import *

window = Tk()

# bg is for background
# fg is for textcolor

l1 = Label(window, text="A", bg="red", fg="white")
l1.pack(side=LEFT, fill=X, expand=1)

l2 = Label(window, text="B", bg="green", fg="white")
l2.pack(side=LEFT, fill=BOTH, expand=1)

l3 = Label(window, text="C", bg="blue", fg="white")
l3.pack(side=LEFT, expand=1, fill=X)

window.mainloop()

