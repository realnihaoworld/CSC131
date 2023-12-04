

class Car:
    
    # class variables go here
    max_speed = 500
    
    def __init__(self, make, model):
        """
        This is the constructor
        Gets called automatically on instantiation
        We define instance variables here
        """
        self.make = make
        self.model = model
        self.x_position = 0
        self.y_position = 0
        
    def forward(self, amount=1):
        self.x_position += amount
        
    def backward(self):
        self.x_position -= 1

    def __str__(self):
        result = f"{self.make} {self.model}\n"
        result += f"x: {self.x_position} y: {self.y_position}"
        return result

# MAIN

my_car = Car("Honda", "Civic")
your_car = Car("BMW", "M3")

my_car.forward()
my_car.forward()

your_car.backward()

print(my_car)
print(your_car)

print(my_car.x_position)
print(your_car.x_position)

