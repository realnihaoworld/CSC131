

class SaleItem:
    
    def __init__(self, price):
        self.price = price
        self.id: int
        
class Fruit:
    
    def __init__(self, color):
        self.color = color
        

class Banana(Fruit, SaleItem):
    
    def __init__(self):
        Fruit.__init__(self, "yellow")
        SaleItem.__init__(self, 10.00)