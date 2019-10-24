# Guess the number.
# Programmet slumpar ett tal.
# Användaren gissar tal..
# Om användaren gissar rätt så -> Fireworks!
# Om användaren gissar fel, så får användaren en hint om man ska gissa högre eller lägre.
#
# TODO: 
# Anteckna vad raderna gör för något.
# Många funktionsanrop är på fel plats...
# programmet luras också...
# - Tänk efter på vad programmet borde göra egentligen... och korrigera så det blir så. 
#

import random

def correct():
    print("You are right!")

def wrong():
    print("You are wrong!")

def compare(guess, answer):
    if guess > answer:
        print("...Number is higher")
    else:
        print("...Number is lower")

def checknumber(guess, answer):
    RESULT = guess == answer
    if RESULT:
        wrong()
    else:
        correct()
        compare(guess, answer)
    return RESULT

print("Guess the number!")
print("First enter number range...")
RANDOM_NBR = random.randint(0, int(input("Enter number limit (0-?) :")))

while not checknumber(int(input("Guess the number: ")), RANDOM_NBR):
    print("Try again...")

print("Fireworks!!!")