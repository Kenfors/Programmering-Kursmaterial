# Ett program som visar hur man kan
# använda variabler på ett finurligt
# sätt i sitt program.

print("\n\n\n\n")

distance = int(input("Skriv antal meter: "))
unit = 'm'


print("Sträckan är", distance, unit, "lång")

multiplier = 'c'
print("...Det är samma som", distance*100, multiplier + unit)


multiplier = 'k'
print("...I kilometer blir det:", distance/1000, multiplier + unit)
