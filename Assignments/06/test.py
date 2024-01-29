SUITS = ["clubs", "diamonds", "hearts", "spades"]


cards = []
for i in range(2, 11):
    for j in range(4):
        cards.append((i, SUITS[j]))
    
print(cards)