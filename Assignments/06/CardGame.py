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
    
    
class Deck():
    
    def __init__(self):
        self.cards = []
        for i in range(2, 11):
            for type in POSSIBLESUITS:
                self.cards.append(Card(i, type))
        # self.cards.append(super().__init__(2, "clubs"))
        # self.cards.append(super().__init__(3, "diamonds"))
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
            for card in self.cards:
                result += f'{card}, '
            result +="]"
            return result
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        if len(self.cards) == 0:
            return None
        else:
            c = self.cards[0]
            del self.cards[0]
            return c
    
    def size(self) -> int:
        return len(self.cards)
    
class Game:
    
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.shuffle()
    
    @property
    def deck(self) -> "Deck":
        return self._deck
    
    @deck.setter
    def deck(self, value) -> None:
        self._deck = value
        
    def start(self):
        print("-" * 40)
        print("Welcome to a basic game.")
        print("You and this program will take turns picking cards.")
        print("The one with the highest value card wins")
        print("-" * 40)
        
        answer = input("Are you ready to start? [Y/N] ")
        
        if answer.lower() == 'y':
            self.play()
        else:
            self.end()
        
    def play(self):
        p1 = self.deck.draw()
        p2 = self.deck.draw()
        print(f"You picked {p1}, and I picked {p2}")
        
        if p1 > p2:
            print("YOU WIN")
        elif p1 == p2:
            print("DRAW")
        else:
            print("I WIN")
        
        answer = input("Would you like to play again? [Y/N] ")
        
        if answer.lower() == 'y' and self.deck.size() != 0:
            self.play()
        elif self.deck.size() == 0:
            print("Not enough cards to play")
            self.end()
        else:
            self.end()
            
    def end(self):
        print("Sorry to see you go")
        print("----Remaining cards-------")
        print(self.deck)
    
