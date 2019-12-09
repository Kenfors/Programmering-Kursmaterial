"""
Program som räknar ut personnummrets kontrollsiffra.

"""

USERINPUT = int(input("Enter your pnumber: "))
N = 9
TOTAL = 0
while N > 0:
    MULTIPLIER = N % 2 + 1
    DIGIT = USERINPUT // 10**N % 10
    ADD = DIGIT * MULTIPLIER
    if ADD >= 10:
        ADD -= 9
    print(MULTIPLIER, "multiplied by:", DIGIT, "=>", ADD)
    TOTAL += ADD
    N -= 1
TOTAL %= 10
KONTROLLSIFFRA = 10 - TOTAL
KONTROLLSIFFRA = int(KONTROLLSIFFRA % 10)
print("Kontrollsiffra: ", KONTROLLSIFFRA) 
print("Your result was: ", KONTROLLSIFFRA == USERINPUT%10)
