from tkinter import *
from CardGame import *

ROWS = 4
COLUMNS = 4

window = Tk()

img = PhotoImage(file='./images/default.png')

window.title("CSC131 Card Game")
window.geometry('1000x1000')

# Text at the top showing which side is the computer and the person
l1 = Label(window, text="Computer picked")
l1.grid(row=0, column=0, sticky=W, ipadx=20)

l2 = Label(window, text="You picked")
l2.grid(row=0, column=4, sticky=E, ipadx=20)

# Picture of the cards
p1 = Label(window, image=img)
p1.grid(row=1, column=0, sticky=W)

p2 = Label(window, image=img)
p2.grid(row=1, column=4, sticky=E)

# Dynamic text that displays the winner
l3 = Label(window, text="Who wins?", font=('Arial', 25))
l3.grid(row=2, columnspan=10)

# The buttons that allow you to play, restart, or quit the game
b1 = Button(window, text="Play", background='light blue')
b1.grid(row=3, column=0, sticky=W)

b2 = Button(window, text="Restart", background='light blue')
b2.grid(row=3, column=1, sticky=W)

b3 = Button(window, text="Quit", background='light blue')
b3.grid(row=3, column=4, sticky=E)

# loops through all the columns so that each one has a weight of 1
for i in range(COLUMNS):
    window.columnconfigure(i, weight=1)
    
window.mainloop()