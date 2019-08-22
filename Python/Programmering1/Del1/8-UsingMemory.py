# Ett program som visar hur man kan
# använda variabler på ett finurligt
# sätt i sitt program.

print("\n\n\n\n")

distance = 3
suffix = 'm'


print("Sträckan är", distance, suffix, "lång")

prefix = 'c'
print("...Det är samma som", distance*100, prefix + suffix)


prefix = 'k'
print("...I kilometer blir det:", distance/1000, prefix + suffix)


