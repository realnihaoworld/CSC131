from room import Room
#import pygame

room1 = Room("Living Room")
room2 = Room("Kitchen")
r3 = Room("bath")
room1.add_exit("east", room2)
room1.add_exit("south", r3)
room1.add_item("shield", "made of wood")

print(room1.exit_destinations)