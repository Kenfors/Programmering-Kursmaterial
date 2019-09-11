import turtle

TUR = turtle.Turtle()

color = input("Choose color: ")
scale = int(input("Choose scale: "))
# INPUT
#
TUR.fillcolor(color)
TUR.speed(0)

TUR.begin_fill()
for i in range(180):
    TUR.forward(2 * scale)
    TUR.left(2)
TUR.end_fill()













turtle.done()