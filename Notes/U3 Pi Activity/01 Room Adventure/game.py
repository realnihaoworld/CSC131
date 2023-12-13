from room import Room
from time import sleep

class Game:
    
    def __init__(self):
        self.inventory = []
        self.current_room = None
        self.response = ""
        self.running = True
        self.create_rooms()
    
    
    def create_rooms(self):
        
        # create the rooms
        r1 = Room("Room 1")
        r2 = Room("Room 2")
        r3 = Room("Room 3")
        r4 = Room("Room 4")

        # add exits to the room
        r1.add_exit("east", r2)         # room 1
        r1.add_exit("south", r3)
        
        r2.add_exit("west", r1)         # room 2
        r2.add_exit("south", r4)
        
        r3.add_exit("north", r1)         # room 3
        r3.add_exit("east", r4)
    
        r4.add_exit("north", r2)
        r4.add_exit("west", r3)         # room 4
        r4.add_exit("south", None)
        
        # add items
        r1.add_item("chair", "It has three legs so don't sit in it")
        r1.add_item("desk", "Its a desk it has a couple legs")
        
        r2.add_item("travis_scott", "fortnite")
        r2.add_item("water", "drink water")
        
        r3.add_item("book_shelf", "It has all the harry potter books")
        r3.add_item("chicken_nugget", "singular, from the cafe")
        
        r4.add_item("harold", "old black man")
        r4.add_item("chris-man", "magnet high's spiderman")
        
        # add_grabbable
        r1.add_grabbable("lamp")
        r3.add_grabbable("chicken_nugget")
        r4.add_grabbable("big_mac")
        
        self.current_room = r1
        
    def handle_go(self, noun):
        self.response = "Invalid exit."
        if noun in self.current_room.exit_directions:
            index = self.current_room.exit_directions.index(noun)
            self.current_room = self.current_room.exit_destinations[index]
            self.response = "Room Changed."
    
    def handle_look(self, noun):
        self.response = "Invalid item."
        if noun in self.current_room.items:
            index = self.current_room.items.index(noun)
            self.response = self.current_room.item_descriptions[index]
        
    def handle_take(self, noun):
        self.response = "Invalid Grabbable"
        if noun in self.current_room.grabbables:
            self.inventory.append(noun)
            self.current_room.delete_grabbable(noun)
            self.response = f"Grabbed {noun}"
    
    
    def play(self):
        while self.running:
            
            # did we die?
            if self.current_room is None:
                self.death()
                break
            
            status = f"\n{self.current_room}"
            
            # any game related stuff we want to add to the status
            if len(self.inventory) != 0:
                status += f"\n You are carrying: "  # noqa: F541
                status += ", ".join(self.inventory)
            else:
                status += "\nYou have no items in your inventory"
                
            print(status)
                
            # create a default response for this loop
            self.response = "Invalid input. Try the format [verb] [noun]."
            self.response += "\nI only understand the verbs 'go', 'take', and 'look'."
            self.response += "\nType 'quit' to exit."
            
            # get input from users
            action = input("What would you like to do? ").lower()
            
            if action in ['quit', 'bye', 'q', 'exit']:
                print("Thanks for playing!")
                self.running = False
                
            words = action.split()
            if len(words) == 2:
                verb = words[0]
                noun = words[1]
                
                if verb == "go":
                    self.handle_go(noun)
                elif verb == "look":
                    self.handle_look(noun)
                elif verb == "take":
                    self.handle_take(noun)
                    
            print(self.response)
            sleep(1)
            
    def death(self):
        print("You fell out a window and died.")
        self.running = False
        