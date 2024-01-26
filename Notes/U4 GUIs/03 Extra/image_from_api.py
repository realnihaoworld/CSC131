import requests
from tkinter import *
import PIL.Image
import PIL.ImageTk
import io

window = Tk()

# get a random url of a picture of a dog https://dog.ceo/api/breeds/image/random
response = requests.get(url="https://dog.ceo/api/breeds/image/random")
data = response.json()
print(data)

# get image from random url
response2 = requests.get(url=data["message"], stream=True)

# turn the image into a pillow image, and attach to Tkinter Label widget
pillow_image = PIL.Image.open(io.BytesIO(response2.content))
photoimage = PIL.ImageTk.PhotoImage(pillow_image)

label = Label(window, image=photoimage)
label.pack()

window.mainloop()