


class Card():
    
    def __init__(self):
        pass

    def __str__(self):
        pass

class CardHolder():
    cards : list
    
    def __init__(self):
        pass

    def __str__(self):
        pass
    def pushCard(self, theCard):
        
        self.cards.append(theCard)

        return

    def pickCard(self, position):
        pickedCard = self.cards.pop(position)
        return pickedCard

class CardGame():
    
    def __init__(self):
        pass

    def __str__(self):
        pass

    def Start(self):
        # Töm spelbräde
        # Skapa kortlek/deck
        # Sätt startvärden på players[]

        return


class BlackJack(CardGame): #Ärver ALLT från "CardGame"
    
    def __init__(self):
        super().__init__() #Kör superklassens init funktion.
        

    def __str__(self):
        pass