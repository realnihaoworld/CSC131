

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