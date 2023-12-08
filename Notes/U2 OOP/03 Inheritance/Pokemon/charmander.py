from pokemon import Pokemon

class Charmander(Pokemon):
    
    ELEMENTAL_TYPE = "Fire"
    
    def __init__(self, nickname, level):
        super().__init__(nickname, level)
        self.power_points = 80
    
    def flamethrower(self, other):
        print(f"{self.nickname} used flamethrower on {other.nickname}")
        self.power_points -= 45
        other.current_hp -= 3
    
    def __str__(self):
        result = "Species: Charmander"
        result += f"\nType: {Charmander.ELEMENTAL_TYPE}"
        result += f"\n{Pokemon.__str__(self)}"
        return result