"""
Program som räknar ut personnummrets kontrollsiffra.

"""

USERINPUT = int(input("Enter your pnumber: "))
USERINPUT = str(USERINPUT)

MULT = 2
TOTAL = 0

letter1 = int(USERINPUT[0]) * 2
letter2 = int(USERINPUT[1]) * 1
letter3 = int(USERINPUT[2]) * 2
letter4 = int(USERINPUT[3]) * 1
letter5 = int(USERINPUT[4]) * 2
letter6 = int(USERINPUT[5]) * 1
letter7 = int(USERINPUT[6]) * 2
letter8 = int(USERINPUT[7]) * 1
letter9 = int(USERINPUT[8]) * 2

if letter1 >= 10:
    letter1 = (letter1 % 10) + 1
if letter3 >= 10:
    letter3 = (letter3 % 10) + 1
if letter5 >= 10:
    letter5 = (letter5 % 10) + 1
if letter7 >= 10:
    letter7 = (letter7 % 10) + 1
if letter9 >= 10:
    letter9 = (letter9 % 10) + 1

TOTAL = letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7 + letter8 + letter9
TOTAL %= 10
KONTROLLSIFFRA = 10 - TOTAL
KONTROLLSIFFRA = int(KONTROLLSIFFRA % 10)
print("Kontrollsiffra: ", KONTROLLSIFFRA)
print("Your result was: ", KONTROLLSIFFRA == int(USERINPUT)%10)
