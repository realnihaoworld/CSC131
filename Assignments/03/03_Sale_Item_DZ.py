#####################################################################
# author: Danison Zhang
# date: 12/11/23
# description: 
#####################################################################

# The SaleItem class has a name, cost and price. All three are provided
# as arguments to the constructor. SaleItem also has a profit function
# that returns the profit that the sale of the item would provide.
# SaleItem also has a applySale function that adjusts the price of the
# item using the percentage provided as an argument to that function.
class SaleItem:
    
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
    
    def profit(self):
        pass
    
    def applySale(self):
        pass



############################ MAIN ###################################
########## DO NOT MODIFY ANYTHING BELOW THIS POINT ##################
#####################################################################
# Create 3 items and print them
i1 = SaleItem("shoes", 50, 79.99)
i2 = SaleItem("jeans", 30, 44.99)
i3 = SaleItem("shirt", 20, 29.99)

print("Item\tCost\tPrice\tProfit")
print("-" * 30)
print(f"{i1.name}\t{i1.cost:.2f}\t{i1.price:.2f}\t{i1.profit():.2f}")
print(f"{i2.name}\t{i2.cost:.2f}\t{i2.price:.2f}\t{i2.profit():.2f}")
print(f"{i3.name}\t{i3.cost:.2f}\t{i3.price:.2f}\t{i3.profit():.2f}")
print("-" * 30)

# Try some changes that should be permitted
i1.cost = 30
i2.name = "jorts"
i2.applySale(50)
i3.price = 39.59
i3.applySale(25)

print(f"{i1.name}\t{i1.cost:.2f}\t{i1.price:.2f}\t{i1.profit():.2f}")
print(f"{i2.name}\t{i2.cost:.2f}\t{i2.price:.2f}\t{i2.profit():.2f}")
print(f"{i3.name}\t{i3.cost:.2f}\t{i3.price:.2f}\t{i3.profit():.2f}")
print("-" * 30)

# Try some changes that should NOT be permitted
i1.cost = -20   
i2.price = -2.99
i3.applySale(200)

print(f"{i1.name}\t{i1.cost:.2f}\t{i1.price:.2f}\t{i1.profit():.2f}")
print(f"{i2.name}\t{i2.cost:.2f}\t{i2.price:.2f}\t{i2.profit():.2f}")
print(f"{i3.name}\t{i3.cost:.2f}\t{i3.price:.2f}\t{i3.profit():.2f}")
print("-" * 30)
