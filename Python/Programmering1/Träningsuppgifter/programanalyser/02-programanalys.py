# Stega igenom koden, rad för rad.
# Anteckna hur variabelvärderna förändras.

VAL = 7
DEC = 9.6
VAL += 4
if VAL > 11:
    VAL -= 7
    print("Greater than 11")
VAL = VAL + 20
SUM = VAL + DEC * 4
DEC /= 2
if SUM > 30:
    print("Greater than 30")
    SUM *= -1
DEC += VAL + int(SUM)
if DEC < 0:
    print("Less than Zero")
VAL += 20*DEC
if VAL*-1 > 300:
    print("Bigest number")
elif VAL*-1 > 260:
    print("Bigger number")
elif VAL*-1 > 240:
    print("Big number")
else:
    print("Whatever...")

SUM += 150
VAL = 80 + int(DEC) + int(SUM / 7)

WHATISVAL = int(input("What value has VAL?: "))
if VAL == WHATISVAL:
    print("You are correct")
else:
    print("You are wrong")

WHATISDEC = float(input("What value has DEC?: "))
if DEC == WHATISDEC:
    print("You are correct")
else:
    print("You are wrong")

WHATISSUM = float(input("What walue has SUM?:"))
if SUM == WHATISSUM:
    print("You are correct")
else:
    print("You are wrong")