import turtle
def drawTriangle(size):
    tur.forward(size)
    tur.left(120)
    tur.forward(size)
    tur.left(120)
    tur.forward(size)
    tur.left(120)
def drawSpiral():
    for i in range(40):
        drawTriangle((i +1) * 10)
        tur.left(10)
tur = turtle.Turtle()
tur.speed(0)
tur.hideturtle()
drawSpiral()
turtle.done()
