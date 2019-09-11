import turtle, random

def keep():
    x = head.pos()[0]
    y = head.pos()[0]

    print(head.pos())

    if (x > 300):
        x = 300
        head.left(180)
    if (x < -300):
        x = -300
        head.goto(x, y)
        head.left(180)
    if (y > 300):
        y = 300
        head.goto(x, y)
        head.left(180)
    if (y < -300):
        y = -300
        head.goto(x, y)
        head.left(180)

    print(head.pos())


widthMAX = 300
heightMAX = 300
widthMIN = -300
heightMIN = -300

turtle.setup(widthMAX*2,heightMAX*2)

head = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('pink')
head.speed(0)
head.pensize(3)


while(True):
    head.forward(random.randint(20,60))
    if(random.randint(0, 100) > 50):
        head.left(random.randint(30, 60))
    else:
        head.right(random.randint(90, 120))
    keep()





turtle.done()




    
    
    