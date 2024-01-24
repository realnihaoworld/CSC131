#####################################################################
# author:       Danison Zhang
# date:         1/23/24
# description:  Sale item reloaded
#####################################################################

# An Item has a name, cost and price, all of which are passed in as
# arguments to its constructor. It has accessors and mutators that carry
# out range checking. It also has profit, applySale, and __str__
# functions that carry out the tasks as described in the assignment
# documentation.
class Item:
    
    def __init__(self, name, cost, price):
        self.name = name
        self.cost = cost
        self.price = price
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value:str) -> None:
        self._name = value
    
    @property
    def cost(self) -> float:
        return self._cost
    
    @cost.setter
    def cost(self, value:float) -> None:
        if value < 0:
            self._cost = 0
        else:
            self._cost = value
    
    @property
    def price(self) -> float:
        return self._price
        
    @price.setter
    def price(self, value:float) -> None:
        if value < 0:
            self._price = 0
        else:
            self._price = value
    
    def __str__(self):
        result = f"{self.name}\t{self.cost:.2f}\t{self.price:.2f}"
        return result
    
    def profit(self) -> float:
        return self.price - self.cost
    
    def applySale(self, percent):
        sale = float((100 - percent) / 100)
        self.price *= sale
        
#####################################################################
# A Clothing is an Item. In addition to name, cost and price, it also
# has a brand, and size. It receives all 5 pieces of information as
# arguments to its constructor. It overloads the __str__ function and
# also has appropriate accessors and mutators.
class Clothing(Item):
    
    def __init__(self, name, brand, cost, price, size):
        super().__init__(name, cost, price)
        self.brand = brand
        self.size = size

    @property
    def brand(self) -> str:
        return self._brand
    
    @brand.setter
    def brand(self, value) -> None:
        self._brand = value
    
    @property
    def size(self) -> int:
        return self._size
    
    @size.setter
    def size(self, value:int) -> None:
        if value <= 0:
            self._size = 0
        else:
            self._size = value
    
    def __str__(self):
        result = Item.__str__(self)
        result += f"\t|{self.brand} size:{self.size}"
        return result
    
#####################################################################
# A Food is an Item. In addition to name, cost and price, it also has a
# shelfLife. It only receives name, cost and price as arguments to its
# constructor. It sets all objects created to have a shelfLife of 7 by
# default. It also overloads the __str__ function.
class Food(Item):
    
    def __init__(self, name, cost, price):
        super().__init__(name, cost, price)
        self.shelfLife = 7

    @property
    def shelfLife(self):
        return self._shelfLife
    
    @shelfLife.setter
    def shelfLife(self, value):
        if value <= 0:
            self._shelfLife = 0
        else:
            self._shelfLife = value
            
    def __str__(self):
        result = Item.__str__(self)
        result+= f"\t|expires in {self.shelfLife} days"
        return result
        
#####################################################################
# A Shoe is a Clothing. It only receives cost, price and size as
# arguments to its constructor. It sets all Shoe objects to have a name
# of "Sneakers" and brand of "Nike" by default.
class Shoe(Clothing):
    
    def __init__(self, cost, price, size):
        super().__init__("Crocs", "Nike", cost, price, size)
        

#####################################################################
# A Chips is a Food. It does not receive any arguments for its
# constructor. It sets the name, cost, price and shelfLife to be "Lays",
# 2, 3.50 and 21 respectively.
class Chips(Food):
    
    def __init__(self):
        super().__init__("Lays", 2, 3.50)
        self.shelfLife = 21

#####################################################################
