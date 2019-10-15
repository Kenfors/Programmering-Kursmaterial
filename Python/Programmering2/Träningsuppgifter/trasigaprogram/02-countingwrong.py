# Detta program beräknar resultat från
# de vanliga fyra räknesätten
# ...Men det blir fel!
# Fixxxa...

A = int(input("First number: "))
B = int(input("Second number: "))

RES = A * B
print("The sum is: ", RES)
RES = A - B + A
print("The difference is: ", RES)
RES = A ** B
print("The product is: ", RES)
RES = A // B
print("The kvot is: ", RES)

