"""
Prov i grundläggande programmering och objektorientering
"""

# Fråga 1.
# Vad kommer visas i terminalen när du kör detta.
values = []
times = 0

values.append(0)
times += 1

while (times <= 10):
    print("count: ", times)
    if(times < 5):
        values.append(times)
    times += (5 - 2 * 2)

print(values)



# Fråga 2.
# Följande program innehåller två feta fel
# Vilka är felen?
# Föreslå förändringar som rättar till det.

def countSheep(num):
    print("sheep number:", num)
    print("ZzZzZ")

maxiterations = "100"
iterations = 0

while (iterations < maxiterations):
    countSheep(iterations)
    print("zzzzZZZ")


# Fråga 3
# Vad kommer visas i terminalen vid körning
# - Användaren skriver in 4, sedan 3

num = int(input("Number: "))
multiplier = int(input("Multiplier: "))

products = []
i = 0
while(i < 10):
    products.append(str(i * num * multiplier))
    i += 1

for prod in products:
    prod += " km/h"
    print("Speed: ", prod)
    

# Fråga 4
# Vad kommer visas i terminalen vid körning

class StoreItem():
    name : str
    price : int
    stock : int

    def __init__(self, n, p, s):
        self.name = n
        self.price = p
        self.stock = s

    def __str__(self):
        return ("\nItem: " + self.name 
                + " \nPrice: " + str(self.price) 
                + "$ \nIn stock: " + str(self.stock) + "pieces")

flowers = StoreItem("Tulips", 50, 347)
foods = StoreItem("Sandwich", 20, 12)

print(flowers)
print(foods)
