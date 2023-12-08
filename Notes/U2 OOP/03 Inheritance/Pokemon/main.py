from pokemon import Pokemon
from pikachu import Pikachu
from charmander import Charmander

# main

greg = Pokemon("gregor", 99)
print(greg)

p1 = Pikachu(40)
print(p1) # method lookup

charly = Charmander("Charly", 34)
print(charly)

p1.thunderbolt(greg)
print(greg)
print(p1)