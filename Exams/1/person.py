class Person:
    number_of_faces = 1
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        self._name = val
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, val):
        self._age = val
    
    def observe_birthday(self):
        self.age += 1
    
    def __str__(self):
        return f"Name: {self.name}; Age: {self.age}"

class Student(Person):
    
    def __init__(self, school):
        Person.__init__(self, None, None)
        self.school = school
    
    def __str__(self) -> str:
        return super().__str__() + f'; Attends: {self.school}'

p = Person('Amanda', 15)
p.age = 10

s = Student('LA Tech')
s._age = 12
s.observe_birthday()

print(s)