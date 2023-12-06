# Inheritance
# Inheritance is a "is-a" relationship

class Pokemon:

    def __init__(self, nickname, level):
        self.nickname = nickname
        self.level = level if level > 0 else 1
        self.current_hp = 20
        self.power_points = 10
        
    @property
    def nickname(self):
        return self._nickname
    
    @nickname.setter
    def nickname(self, new_nickname):
        self._nickname = new_nickname
    
    @property
    def level(self):
        return self._level
        
    @level.setter
    def level(self, new_level):
        if new_level >= 0:
            self._level = new_level
        else:
            raise Exception("The level has to be positive.")
        
    def __str__(self):
        result = f"Nickname: {self.nickname}"
        result += f"\nLevel: {self.level}"
        result += f"\nHP: {self.current_hp}"
        result += f"\nPP: {self.power_points}"
        return result


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