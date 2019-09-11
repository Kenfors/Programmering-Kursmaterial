import turtle, random


def holdOnScreen():
    X = TUR.pos()[0]
    Y = TUR.pos()[1]
    print("X pos: ", X, Y)

    OutOfBounds = (X > 200) or (X < -200) or (Y > 200) or (Y < -200) # Sparar True/False
    if OutOfBounds:
        #Lösning 3
        TUR.penup()
        TUR.goto(0,0)
        TUR.pendown()

        # Lösning 2
        #TUR.setheading(TUR.towards(0, 0))
        #TUR.forward(SPEED)

        # Lösning 1
        #TUR.left(180)
        #TUR.forward(SPEED)


SPEED = int(input("Choose speed: "))
TURN = int(input("Choose turn: "))

TUR = turtle.Turtle()
TUR.speed(0)

while True:
    ANGLE = random.randint(-3, 3) * TURN
    holdOnScreen()
    TUR.forward(SPEED)
    TUR.left(ANGLE)


# LOOP, infinite
# CONDITIONS, hold on screen 
# kanske FUNCTIONS, contain code.



turtle.done()
