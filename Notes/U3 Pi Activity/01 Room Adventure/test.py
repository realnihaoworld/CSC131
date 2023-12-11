from room import Room

room1 = Room("Living Room")
room2 = Room("Kitchen")
room1.add_exit("east", room2)

print(room1)