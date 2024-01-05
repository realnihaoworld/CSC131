from room import Room
from time import sleep
import random


class Game:

    def __init__(self):
        self.pokedex = []
        self.current_room = None
        self.response = ""
        self.running = True
        self.create_rooms()
        self.pokeball_count = 10


    def create_rooms(self):

        # create rooms
        r1 = Room("Kanto region")
        r2 = Room("Hoenn Region")
        r3 = Room("Johto region")
        r4 = Room("Sinnoh region")
        r5 = Room("Alola region")
        r6 = Room("Unova region")
        r7 = Room("Paldea region")

        # add exits
        r1.add_exit("north", r5)
        r1.add_exit("east", r2)
        r1.add_exit("south", r3)
        r1.add_exit("west", r6)

        r2.add_exit("west", r1)
        r2.add_exit("south", r4)

        r3.add_exit("north", r1)
        r3.add_exit("east", r4)

        r4.add_exit("north", r2)
        r4.add_exit("west", r3)

        r5.add_exit("south", r1)

        r6.add_exit("south", r7)
        r6.add_exit("east", r1)

        r7.add_exit("north", r6)
        r7.add_exit("east", r3)

        # add items

        r1_pokeballs_chest = random.randint(1, 2)
        if r1_pokeballs_chest == 1:
            r1.add_item("chest", "Upon opening, I notice a bag of pokeballs inside")
        r1.add_item("charmander", "The fire on the tip of its tail is a measure of its life. "
                                  "If healthy, its tail burns intensely.")
        r1.add_item("squirtle", "It shelters itself in its shell then strikes back with spouts "
                                "of water at every opportunity.")
        r1.add_item("bulbasaur", "For some time after its birth, it grows by gaining nourishment"
                                 " from the seed on its back")
        legendary_spawn_rate = random.randint(1, 5)
        if legendary_spawn_rate == 2:
            r1.add_item("articuno", "In terms of physical strength, Articuno is the strongest "
                                    "out of the three Legendary Birds;"
                                    " as shown in the anime, Articuno is able to lift one of "
                                    "Team Rocket's mechas with its talons.")
            r1.add_grabbable("articuno")

        r2_pokeballs_chest = random.randint(1, 2)
        if r2_pokeballs_chest == 1:
            r2.add_item("chest", "Upon opening, I notice a bag of pokeballs inside")
            r2.add_grabbable("pokeballs")
        r2.add_item("golbat", "Flitting around in the dead of night, it sinks its fangs into "
                             "its prey and drains a nearly fatal amount of blood")
        r2.add_item("ninetales", "Each of its nine tails is imbued with supernatural power, "
                                "and it can live for a thousand years.")
        r2.add_item("dugtrio", "Its three heads move alternately, driving it through tough soil"
                              " to depths of over 60 miles")
        legendary_spawn_rate = random.randint(1, 5)
        if legendary_spawn_rate == 2:
            r2.add_item("zapdos", "When Zapdos flaps its glittering wings, it releases "
                                 "electricity that can potentially cause thunderstorms."
                                 " It produces massive crackling and snapping sounds when it flies; these are "
                                 "attributed to the lightning bolts it sheds when airborne."
                                 " When stricken by lightning, it gains power. Zapdos reportedly appears only during"
                                 " thunderstorms, and is said to live among thunderclouds."
                                 " However, it is rarely seen.")
            r2.add_grabbable("zapdos")

        r3_pokeballs_chest = random.randint(1, 2)
        if r3_pokeballs_chest == 1:
            r3.add_item("chest", "Upon opening, I notice a bag of pokeballs inside")
            r3.add_grabbable("pokeballs")
        r3.add_item("wartortle", "It is said to live 10,000 years. Its furry tail is popular "
                                 "as a symbol of longevity.")
        r3.add_item("fearow", "It has the stamina to fly all day on its broad wings."
                              " It fights by using its sharp beak")
        r3.add_item("pikachu", "It occasionally uses an electric shock to recharge a fellow"
                               " Pikachu that is in a weakened state")
        legendary_spawn_rate = random.randint(1, 5)
        if legendary_spawn_rate == 2:
            r3.add_item("moltres", "Moltres sheds embers with every flap of its wings, creating"
                                   " a brilliant flash of flames."
                                   " By dipping itself into the magma of an active volcano, this Pokémon can "
                                   "heal itself. "
                                   "It migrates to the south with the coming of spring and is said to bring "
                                   "an early springtime to cold lands."
                                   " However, it is rarely seen in normal occasions.")
            r3.add_grabbable("moltres")

        r4_pokeballs_chest = random.randint(1, 2)
        if r4_pokeballs_chest == 1:
            r4.add_item("chest", "Upon opening, I notice a bag of pokeballs inside")
            r4.add_grabbable("pokeballs")
        r4.add_item('arcanine', "The sight of it running over 6,200 miles in a single day "
                                "and night has captivated many people.")
        r4.add_item("machamp", "Its four muscled arms slam foes with powerful punches and "
                              "chops at blinding speed.")
        r4.add_item("electabuzz", "Research is progressing on storing lightning in Electabuzz"
                                 " so this energy can be used at any time")
        legendary_spawn_rate = random.randint(1, 5)
        if legendary_spawn_rate == 2:
            r4.add_item("mewto", "As evidence of its immense power, Mewtwo is by far one of "
                                 "the most domineering Pokémon in the series."
                                 " Its power is so great to the point where it can endure immense torture in Mewtwo"
                                 " Returns, and teleport a lake miles long underground.")
            r4.add_grabbable("mewto")

        r5_pokeballs_chest = random.randint(1, 2)
        if r5_pokeballs_chest == 1:
            r5.add_item("chest", "Upon opening, I notice a bag of pokeballs inside")
            r5.add_grabbable("pokeballs")
        r5.add_item("dodtrio", "When Doduo evolves into this odd breed, one of its heads"
                              " splits into two. It runs at nearly 40 mph")
        r5.add_item("scyther", "The sharp scythes on its forearms become increasingly sharp"
                              " by cutting through hard objects.")
        r5.add_item("gyarados", "Once it begins to rampage, a Gyarados will burn everything"
                               " down, even in a harsh storm.")
        legendary_spawn_rate = random.randint(1, 5)
        if legendary_spawn_rate == 2:
            r5.add_item("regigigas", 'Regigigas towed the continents into their current'
                                    ' arrangement using nothing more than rope.'
                                    ' It is thought to communicate via both telepathy and the flashing lights'
                                    ' on its head.'
                                    ' According to legend, Regigigas crafted three Pokémon in its likeness out'
                                    ' of clay, ice, and magma')
            r5.add_grabbable("regigigas")

        r6_pokeballs_chest = random.randint(1, 2)
        if r6_pokeballs_chest == 1:
            r6.add_item("chest", "Upon opening, I notice a bag of pokeballs inside")
            r6.add_grabbable("pokeballs")
        r6.add_item("dragonite", "It is said to make its home somewhere in the sea. It guides"
                                " crews of shipwrecks to shore")
        r6.add_item("rhydon", "Standing on its hind legs freed its forelegs and made it smarter."
                             " It is very forgetful, however.")
        r6.add_item("espeon", "Its fur is so sensitive, it can feel minute shifts in the air and"
                             " predict the weather...and its foes thoughts.")
        legendary_spawn_rate = random.randint(1, 5)
        if legendary_spawn_rate == 1:
            r6.add_item("reshiram", "Flames spew from its tail as it flies through the sky like"
                                   " a jet airplane."
                                   " It's said that this Pokémon will scorch the world.")
            r6.add_grabbable("reshiram")

        r7_pokeballs_chest = random.randint(1, 2)
        if r7_pokeballs_chest == 1:
            r7.add_item("chest", "Upon opening, I notice a bag of pokeballs inside")
            r7.add_grabbable("pokeballs")
        r7.add_item("dusclops", "It seeks drifting will-o-the-wisps and sucks them into its empty"
                               " body. What happens inside is a mystery.")
        r7.add_item("rayquaza", "It lives in the ozone layer far above the clouds and cannot be"
                               " seen from the ground.")
        r7.add_item("hydreigon", "It responds to movement by attacking. This scary, three-headed"
                                " Pokémon devours everything in its path!")
        legendary_spawn_rate = random.randint(1, 5)
        if legendary_spawn_rate == 1:
            r7.add_item("zekrom", 'Mythology tells us that if people lose the righteousness in'
                                 ' their hearts, their kingdoms will be razed by Zekroms lightning.')
            r7.add_grabbable("zekrom")



        # add Grabbables
        r1.add_grabbable("charmander")
        r1.add_grabbable("squirtle")
        r1.add_grabbable("bulbasaur")
        r1.add_grabbable("pokeballs")

        r2.add_grabbable("golbat")
        r2.add_grabbable("ninetales")
        r2.add_grabbable("dugtrio")

        r3.add_grabbable("wartortle")
        r3.add_grabbable("fearow")
        r3.add_grabbable("pikachu")

        r4.add_grabbable("arcanine")
        r4.add_grabbable("machamp")
        r4.add_grabbable("electabuzz")

        r5.add_grabbable("dodtrio")
        r5.add_grabbable("scyther")
        r5.add_grabbable("gyarados")

        r6.add_grabbable("dragonite")
        r6.add_grabbable("rhydon")
        r6.add_grabbable("espeon")

        r7.add_grabbable("dusclops")
        r7.add_grabbable("rayquaza")
        r7.add_grabbable("hydreigon")

        self.current_room = r1



    def handle_go(self, noun):
        self.response = "That side is completely surrounded by water, I can't go there."
        if noun in self.current_room.exit_directions:
            index = self.current_room.exit_directions.index(noun)
            self.current_room = self.current_room.exit_destinations[index]
            self.response = "After a long journey, I finally made it to a new region."

    def handle_look(self, noun):
        self.response = "Invalid Item."
        if noun in self.current_room.items:
            index = self.current_room.items.index(noun)
            self.response = self.current_room.item_descriptions[index]

    def handle_take(self, noun):
        self.response = "I can't do that."
        if noun in self.current_room.grabbables and self.pokeball_count > 0:

            if noun != "pokeballs":
                self.pokeball_count -= 1
                capture = random.randint(1, 3)
                shiny = random.randint(1, 12)
                ran = random.randint(1, 5)


                if 1 == shiny:
                    for i in range(0, 4):
                        print("Capturing")
                        sleep(.4)
                        print(".")
                        sleep(.4)
                        print(".")
                        sleep(.4)
                        print(".")
                        sleep(.4)
                    self.pokedex.append(f"Shiny {noun}")
                    self.current_room.delete_grabbable(noun)
                    self.current_room.delete_item(noun)
                    self.response = (f"I have {self.pokeball_count} pokeballs left "
                                 f"I just caught a Shiny {noun}. That is super rare. "
                                 f"There is only a 1 in 12 chance of a pokemon being shiny. Lets go capture some more!")

                elif 1 == ran:
                    for i in range(0, 2):
                        print("Capturing")
                        sleep(.4)
                        print(".")
                        sleep(.4)
                        print(".")
                        sleep(.4)
                        print(".")
                        sleep(.4)
                    self.current_room.delete_grabbable(noun)
                    self.current_room.delete_item(noun)
                    self.response = (f"Aw man, the pokemon has escaped. "
                                     f"I have {self.pokeball_count} pokeballs left")

                elif 1 == capture:
                    for i in range(0, 3):
                        print("Capturing")
                        sleep(.4)
                        print(".")
                        sleep(.4)
                        print(".")
                        sleep(.4)
                        print(".")
                        sleep(.4)
                    self.pokedex.append(noun)
                    self.current_room.delete_grabbable(noun)
                    self.current_room.delete_item(noun)
                    self.response = (f"I just caught a {noun}. Lets go capture some more! "
                                     f"I have {self.pokeball_count} pokeballs left")

                else:
                    for i in range(0, 2):
                        print("Capturing")
                        sleep(.4)
                        print(".")
                        sleep(.4)
                        print(".")
                        sleep(.4)
                        print(".")
                        sleep(.4)
                    self.response = (f"I didn't capture it this time. I should try again! "
                                     f"I have {self.pokeball_count} pokeballs left")
            elif noun == "pokeballs":
                self.pokeball_count += 5
                self.current_room.delete_grabbable("pokeballs")
                self.current_room.delete_item("chest")
                self.response = f"I grabbed the pokeballs"


    def play(self):
        while self.running:

            # did we die?
            if self.current_room == None:
                self.death()
                break

            status = f"\n{self.current_room}"

            #any game related stuff
            if len(self.pokedex) != 0:
                status += f"\n I have captured: "
                status += ', '.join(self.pokedex)
            else:
                status += "\nI have no pokemon in my pokedex."

            print(status)

            # create a default response
            self.response = "Invalid Input. Try the format [verb] [noun]."
            self.response += "\nI only understand the verbs 'go', 'capture', 'look', and 'take'."
            self.response += "\nType 'quit' to exit."

            action = input("What should I do?").lower()

            if action in ["quit", "bye","q","exit"]:
                self.running = False
                break

            words = action.split()
            if len(words) == 2:
                verb = words[0]
                noun = words[1]

                if verb == "go":
                    self.handle_go(noun)
                elif verb == "look":
                    self.handle_look(noun)
                elif verb == "capture" or verb == "take":
                    self.handle_take(noun)

            print(self.response)
            sleep(1)



    def death(self):
        print("You died")
        self.running = False

