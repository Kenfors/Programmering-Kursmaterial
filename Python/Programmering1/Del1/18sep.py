"""
Repetition av:
- Variabler
- Input
- Typer och konvertering

Genomgång av beräkningar:
- Nummerberäkningar
- Jämförelseberäkningar
"""

# Variabler, Input och typkonvertering

MYTEXT = "text text text text"
#print(MYTEXT) 
MYNUMBER = 55
#print(MYNUMBER)
MYDECIMAL = 3.14
#print(MYDECIMAL)


#print(type(True))

# Beräkningar med nummer
A = 5
B = 3
RES = A / B
#print(type(RES))


# Jämförelseberäkningar

VALUE1 = 21
VALUE2 = 21
#print(VALUE1 == VALUE2) # == LIKADANA?
#print(VALUE1 > VALUE2) # > A Större än B ?
#print(VALUE1 < VALUE2) # < A Mindre än B ?
#print(VALUE1 <= VALUE2) # <= A Större eller Lika med B ?
#print(VALUE1 >= VALUE2) # <= A Mindre eller Lika med B ?





# Övning
# - Input  (typkonvertering)
#   int(input("text till användaren"))

# Skriv ett program där:
# Programmet hittar på ett tal
# Använadren gissar talet
# Programmet skriver ut om det var rätt eller fel

import random
RANDOMTAL = random.randint(0, 10)


INPUTTAL  = int(input("Guess number from 1 - 10: "))
while (RANDOMTAL != INPUTTAL):
    #Hoppa in ett steg...
    INPUTTAL = int(input("Guess again: "))


print("Gratz")





