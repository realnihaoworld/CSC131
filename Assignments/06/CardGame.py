#####################################################################
# author:      Danison Zhang    
# date:       1/28/24
# description: program 6
#####################################################################

# import the shuffle and seed functions from the random library.
import random

# set the seed
random.seed(9876543210)

# define the possible suits that the cards can have using a list.
POSSIBLESUITS = ["clubs", "diamonds", "hearts", "spades"]

class Card:
    
    def __init__(self, number: int, suit: str):
        self.number = number
        self.suit = suit
    
    @property
    def number(self) -> int:
        return self._number
    
    @number.setter
    def number(self, value) -> None:
        if 2 <= value <= 10 and isinstance(value, int):
            self._number = value
        else:
            self._number = 2
    
    @property
    def suit(self) -> str:
        return self._suit
    
    @suit.setter
    def suit(self, value) -> None:
        if value.lower() in POSSIBLESUITS:
            self._suit = value
        else:
            self._suit = "clubs"
            
    # operator overloading
    
    def __str__(self):
        return f"{self.number} of {self.suit}"
    
    def __eq__(self, other: "Card") -> bool:
        if self.number == other.number:
            return True
        return False
        
    def __gt__(self, other: "Card") -> bool:
        if self.number > other.number:
            return True
        return False
        
    def __lt__(self, other: "Card") -> bool:
        if self.number < other.number:
            return True
        return False
    
    
class Deck(Card):
    
    def __init__(self):
        self.cards = []
        for i in range(2, 11):
            for j in range(4):
                self.cards.append(super().__init__(i, POSSIBLESUITS[j]))
        

    @property
    def cards(self) -> list:
        return self._cards
        
    @cards.setter
    def cards(self, value) -> None:
        self._cards = value
    
    def __str__(self):
        if len(self.cards) == 0:
            return "[--empty--]"
        else:
            result = "["
            for _ in self.cards:
                result += f'{Card.__str__(self)}, '
            result +="]"
            return result
class Game:
    pass
