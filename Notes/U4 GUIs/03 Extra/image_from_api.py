import requests
from tkinter import *
import PIL.Image
import PIL.ImageTk
import io
from random import randint

window = Tk()

# get a random url of a picture of a dog https://dog.ceo/api/breeds/image/random | https://pokeapi.co/api/v2/pokemon
# https://dog.ceo/api/breeds/image/random
rand = randint(0, 1000)
response = requests.get(url=f"https://pokeapi.co/api/v2/pokemon/{rand}/")
data = response.json()
print(rand)
#print(data)

# get image from random url
response2 = requests.get(url=data["sprites"]["front_default"], stream=True)

# turn the image into a pillow image, and attach to Tkinter Label widget
pillow_image = PIL.Image.open(io.BytesIO(response2.content))
photoimage = PIL.ImageTk.PhotoImage(pillow_image)

label = Label(window, image=photoimage)
label.pack()

window.mainloop()