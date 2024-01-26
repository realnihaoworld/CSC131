from tkinter import *

window = Tk()

# bg is for background
# fg is for textcolor

l1 = Label(window, text="A", bg="red", fg="white")
l1.pack(fill=X)

l2 = Label(window, text="B", bg="green", fg="white")
l2.pack(fill=X)

l3 = Label(window, text="C", bg="blue", fg="white")
l3.pack(fill=X)

window.mainloop()