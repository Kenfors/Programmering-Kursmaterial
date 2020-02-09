
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

