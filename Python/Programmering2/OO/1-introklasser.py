#
#
#
#
#

#Grundstruktur
class classname(object):
    pass

# Skapa en klass
# __str__ returnerar en bra text att skrivas ut.
# __init__

class Djur():
    namn : str
    color : str
    weight : int
    length : int

    def __init__(self, n, c, w, l):
        self.namn = n
        self.color = c
        self.weight = w
        self.length = l

    def __str__(self):
        text = self.color + " "
        text += self.namn + " "
        text += str(self.weight) + "kg "
        text += str(self.length) + "m"

        return text


# Object vs Class

katt = Djur("Katt", "Svart", 2, 1)


#annankatt = Djur()
#aannankatt.namn = "Tiger"
#annankatt.color = "Orange med svarta ränder"
#annankatt.length = 2
#annankatt.weight = 250

print(katt)

#print(annankatt)


