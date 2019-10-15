# Skriv ett program som printar alla tal mellan 0 och 100000!
# Alla primtal till visst tal.

# Problem
# Programmet skriver inte alls ut alla primtal :(
# Laga / Fixa..


LIMIT = int(input("Primtal upp till: ")) # Läs in ett tal från tangentbord
NUM = 2
while NUM < LIMIT:
    DEMOMINATOR = NUM -2
    while NUM > 1:
        if NUM % DEMOMINATOR == 0:
            break?
        DEMOMINATOR -= 2
    else:
        print(NUM, "Is Not Prime number!")
    NUM += 1



