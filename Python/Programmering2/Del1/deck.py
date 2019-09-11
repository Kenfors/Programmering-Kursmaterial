

def showCard(card):
    pass

deck = []

for suit in range(4):
    for rank in range(13):
        card = (suit, rank)
        deck.append(card)

print(deck)