

class Car:
    
    def __init__(self):
        self.horsepower = horsepower: int
        self.weight = weight: int
        self.make = make
        self.model = model
    
    @property
    def horsepower(self):
        return self._horsepower
    
    @horsepower.setter
    def horsepower(self, value):
        self._horsepower = value

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        self._weight = value