from tkinter import *
import PIL.Image 
import PIL.ImageTk

window = Tk()

pillow_image = PIL.Image.open("pokeball.png")
resized_image = pillow_image.resize((1000, 1000))
photoimage = PIL.ImageTk.PhotoImage(resized_image)

label = Label(window, image=photoimage)
label.grid()

window.mainloop()