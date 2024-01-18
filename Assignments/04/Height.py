#####################################################################
# author:       
# date:        
# description: 
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
