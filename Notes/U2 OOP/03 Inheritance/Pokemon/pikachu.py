from pokemon import Pokemon

class Pikachu(Pokemon):
    
    # class variables here
    ELEMENTAL_TYPE = 'Electric'
    
    def __init__(self, level):
        # super().__init__("Pikachu", level)
        Pokemon.__init__(self, "Pikachu", level)
        
    def thunderbolt(self, other: Pokemon):
        print(f"{self.nickname} used thunderbolt on {other.nickname}")
        self.power_points -= 2
        other.current_hp -= 3