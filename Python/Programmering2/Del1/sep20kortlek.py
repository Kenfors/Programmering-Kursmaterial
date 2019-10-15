"""
Kortlek
Där vi använder "for each"-loop
för att byggga upp kortleken.

"""

DECK = []
SUITS = ['of Hearts', 'of Spades', 'of Diamonds', 'of Clubs']
SUITS_SHORT = ['H', 'S', 'D', 'C']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# For each. for/in

#för varje sak i den här listan... gör det här:
for suit in SUITS:
    #print("Doing:", suit)
    for rank in RANKS:
        DECK.append((rank, suit))
        #
        #
for card in DECK:
    #print(card)
    pass



def printCard(current_card):
    print(RANKS[current_card['rankValue']], SUITS[current_card['suitValue']])


def printFancyCard(current_card):
    print('#########')
    print('#')
    print('#')
    print('#')
    print('#')
    print('#')
    print('#########')


DECK2 = []
for suit in range(4):
    for rank in range(13):
        CARD = {
            'suitValue' : suit,
            'rankValue' : rank,
        }
        DECK2.append(CARD)


for C in DECK2:
    printCard(C)


# 0 1 2 3
# 0 0
# 1 1
# 2 2
# 3
# ..
# 12



# H, S, D, C
# 2  2 
# 3  3
# 4  4
# ----
# Q
# K 
# A  A