#from room import Room
import pygame

# room1 = Room("Living Room")
# room2 = Room("Kitchen")
# room1.add_exit("east", room2)
# room1.add_item("shield", "made of wood")

# print(room1)
# print()
# print(room2)

pygame.mixer.init()
death_sfx = pygame.mixer.Sound('soundfiles/death.mp3')


while True: 
    death_sfx.play()