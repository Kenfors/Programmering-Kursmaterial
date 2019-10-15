#
#



# Skriv ett program som printar alla tal mellan 0 och 100000!


# Alla primtal till visst tal.


LIMIT = int(input("Primtal upp till: ")) # Läs in ett tal från tangentbord
NUM = 2
while NUM < LIMIT:
    DEMOMINATOR = NUM -1
    while DEMOMINATOR > 1:
        if NUM % DEMOMINATOR == 0:
            break
        DEMOMINATOR -= 1
    else:
        print(NUM, "Is A Prime number!")
    NUM += 1



