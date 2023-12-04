

class Dog:

    # class variables
    sound = "i am a dog"
    
    def __init__(self, name):
        self.name = name
        self.favorite_chew = "bone"
    
    @property
    def favorite_chew(self):
        return self._favorite_chew
    
    @favorite_chew.setter
    def favorite_chew(self, value):
        if len(value) >= 2:
            self._favorite_chew = value
    
    def bark(self):
        print(Dog.sound)
        
    def greet(self, other_dog):
        self.bark()
        print(f"My name is {self.name}")
        other_dog.bark()
        print(f"Nice to meet you, my name is {other_dog.name}")
    
    def __str__(self):
        return f"Name: {self.name}\tFavorite Chew: {self.favorite_chew}"
        