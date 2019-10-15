# Skriv kommentarer till alla kommandon.
# Skriv även ner vilka värden som sparas, och hur dom förändras...

import turtle

PENCIL = turtle.Turtle()
PENCIL.speed(5) # Sätter hastigheten till "Lagom"

PARAMETER = 50
PENCIL.circle(PARAMETER)
PENCIL.forward(PARAMETER)
PARAMETER -= 10
PENCIL.forward(PARAMETER)
PENCIL.circle(PARAMETER)
PENCIL.forward(PARAMETER)
PARAMETER -= 20
PENCIL.circle(PARAMETER)

PENCIL.back(100)
PENCIL.speed(0) # Sätter hastigheten till "Skitsnabb"

LOOPER = PARAMETER
while LOOPER > 0:
    PENCIL.circle(LOOPER)
    LOOPER -= 2
PENCIL.speed(5)

PENCIL.penup() # Lyften penseln
PENCIL.goto(PARAMETER*-1, PARAMETER)
PENCIL.pendown()

LOOPER = PARAMETER*2
EXTENT = 360
PENCIL.speed(0)
while LOOPER > 0:
    PENCIL.circle(LOOPER,EXTENT)
    LOOPER -= 2
    EXTENT -= 15
PENCIL.speed(1)

PARAMETER = 200
PENCIL.forward(PARAMETER)

PENCIL.write("TURTLE!")
PENCIL.left(PARAMETER)
PENCIL.forward(PARAMETER*2)

PENCIL.speed(5)
LIMIT = 0
LOOPER = 90
DIRECTION = 1
while LIMIT < 20:
    PENCIL.circle(LOOPER+5, LOOPER+90, LIMIT+5)
    LOOPER -= 15 * DIRECTION
    if LOOPER < 0:
        DIRECTION = -1
    LIMIT += 1

turtle.done()
