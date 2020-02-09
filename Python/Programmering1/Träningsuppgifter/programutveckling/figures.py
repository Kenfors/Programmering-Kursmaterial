import turtle, random


COLORS = ['red', 'green', 'blue', 'yellow', 'purple', 'magenta']

tur = turtle.Turtle()
tur.speed(0)

def builingsquare(maxsize):
    size = 10
    inc = int(maxsize / 20)
    while (size < maxsize):
        tur.left(inc)
        tur.forward(size)
        tur.left(90)
        tur.forward(size)
        tur.left(90)
        tur.forward(size)
        tur.left(90)
        tur.forward(size)
        tur.left(90)
        size += inc
def circleloop(maxsize):
    size = 10
    inc = int(maxsize / 20)
    while (size < maxsize):
        tur.left(inc)
        tur.circle(size)
        size += inc
    
for i in range(100):
    tur.pencolor(random.choice(COLORS))
    circleloop(200)
    tur.right(20)


turtle.done()
