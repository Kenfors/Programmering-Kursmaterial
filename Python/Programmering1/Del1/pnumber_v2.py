"""
Program som räknar ut personnummrets kontrollsiffra.

"""

USERINPUT = int(input("Enter your pnumber: "))
USERINPUT = str(USERINPUT)

MULT = 2
TOTAL = 0
for letter in USERINPUT:
    letter = int(letter)
    ADD = letter * MULT
    if ADD >= 10:
        ADD -= 9
    TOTAL += ADD
    print(letter, "multiplied by:", MULT, "=>", ADD)
    if MULT == 2:
        MULT = 1
    else:
        MULT = 2

TOTAL %= 10
KONTROLLSIFFRA = 10 - TOTAL
KONTROLLSIFFRA = int(KONTROLLSIFFRA % 10)
print("Kontrollsiffra: ", KONTROLLSIFFRA)
print("Your result was: ", KONTROLLSIFFRA == int(USERINPUT)%10)
