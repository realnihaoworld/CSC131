from tkinter import *

window = Tk()

img = PhotoImage(file='ironman.png')

l1 = Label(window, text="A Label")
l1.grid(row=0, column=0, sticky=W)
# could use sticky
l2 = Label(window, text="Another Label")
l2.grid(row=1, column=0, sticky=E)

l3 = Label(window, text="A third label, centered")
l3.grid(row=2, columnspan = 2)

l4 = Label(window, image=img)
l4.grid(row=0, column=2, columnspan=2, rowspan=2)
# if you were in a function you need
# l4.image = img

e1 = Entry(window)
e1.grid(row=0, column=1)

e2 = Entry(window)
e2.insert(0, "user input")
e2.grid(row=1, column=1)

c1 = Checkbutton(window, text="Some Checkbutton option")
c1.grid(row=3, column=0, columnspan=2)

b1 = Button(window, text="A button")
b1.grid(row=3, column=2)

b2 = Button(window, text="Another button")
b2.grid(row=3, column=3)

window.mainloop()