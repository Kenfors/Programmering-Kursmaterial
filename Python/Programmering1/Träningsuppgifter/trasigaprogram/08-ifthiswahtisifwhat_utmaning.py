# Svårare uppgift.
# Det här är ett totalt meningslöst program som skriver massa olika texter
# beroende på vilket nummer det blir.
# 
# Ditt jobb är att ta bort onödiga bitar.
# Alltså vissa texter i programmet kan aldrig hända!
# Fixa.

import random

RANDNUM = random.randint(0, 10) #Random tal mellan 0 och 10
RANDNUM += 1
if (RANDNUM > 3):
    print("The number is greater than 3...")
    if (RANDNUM < 3):
        print("Number less than 3!")
    if (RANDNUM < 8):
        if(RANDNUM != 8):
            print("...Less than 8")
    else:
        print("...Not less than 8")
        if (RANDNUM == 9):
            print("...Cus its 9")
            while RANDNUM < 100:
                print("Incrementing? or am i?...")
                break
        elif (RANDNUM == 10):
            print("...Cus its 10")
    if (RANDNUM == 1):
        print("Number is 1!")
    print("Number was", RANDNUM)
    RANDNUM = random.randint(0, 10)
    print("Now its something else...")
    if (3 == 9):
        print("I'm a useless print-statement, why?")
    else:
        print("Uugh.")
        GUESS = int(input("Guess the number (0-10): "))
        while (GUESS != RANDNUM):
            GUESS = int(input("Guess better: "))
        else:
            print("...Correct. your guess was a lucky guess i guess")
        


