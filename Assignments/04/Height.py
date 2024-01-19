#####################################################################
# author: Danison Zhang
# date: 1/18/24
# description: Program 4
#####################################################################

# Don't forget to name this file Height.py and place it in the same
# folder as the provided HeightTest.py file so that they can
# automatically find and use each other.

class Height:
    # A constructor that takes in two arguments for the ft and inch
    # respectively. Default values for both parameters are 0.
    def __init__(self, feet=0, inch=0):
        self.feet = feet
        self.inch = inch
        
    ####### Accessors and mutators for instance variables ###########
    @property
    def feet(self) -> int:
        return self._feet
    
    @feet.setter
    def feet(self, value:int) -> None:
        if value < 0:
            self._feet = 0
        else:
            self._feet = value
            
    @property
    def inch(self) -> int:
        return self._inch
    
    @inch.setter
    def inch(self, value:int) -> None:
        if value < 0:
            self._inch = 0
        elif value >= 12:
            self._feet += value // 12
            self._inch = value % 12
        else:
            self._inch = value
    
    ######### other functions e.g. __str__ and inches ###############
    def inches(self):
        total = self.inch + (self.feet * 12)
        return total
        
    def __str__(self):
        return f"{self.feet}' {self.inch}\""
        
    ####### overloaded mathematical and comparison operators ########
    ############## i.e. +, -, <, <=, >, >=, ==, != ##################
    def __add__(self, other: 'Height') -> 'Height':
        total_inches = (self.feet * 12) + (other.feet * 12) + self.inch + other.inch
        feet = total_inches // 12
        inches = total_inches % 12
        result = Height(feet, inches)
        return result
    
    def __sub__(self, other: 'Height') -> 'Height':
        self_inches = (self.feet * 12) + self.inch 
        other_inches = (other.feet * 12) + other.inch
        
        total = self_inches - other_inches
        if total < 0:
            return Height()
            
        feet = total // 12
        inches = total % 12
        
        result = Height(feet, inches)
        return result
        
    def __lt__(self, other: 'Height') -> 'Height':
        if self.inches() < other.inches():
            return True
        return False
    
    def __le__(self, other: 'Height') -> 'Height':
        if self.inches() <= other.inches():
            return True
        return False
    
    def __gt__(self, other: 'Height') -> 'Height':
        if self.inches() > other.inches():
            return True
        return False
        
    def __ge__(self, other: 'Height') -> 'Height':
        if self.inches() >= other.inches():
            return True
        return False
    
    def __eq__(self, other: 'Height') -> 'Height':
        if self.inches() == other.inches():
            return True
        return False
        
    def __ne__(self, other: 'Height') -> 'Height':
        if self.inches() != other.inches():
            return True
        return False