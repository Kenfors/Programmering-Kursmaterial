import turtle, random

def keep():
    x = head.pos()[0]
    y = head.pos()[0]

    if (x > 300):
        head.goto(300, y)
        head.setheading(180)
        head.forward(50)
        return
    if (x < -300):
        head.goto(-300, y)
        head.setheading(0)
        head.forward(50)
        return
    if (y > 300):
        head.goto(x, 300)
        head.setheading(270)
        head.forward(50)
        return
    if (y < -300):
        head.goto(x, -300)
        head.setheading(90)
        head.forward(50)
        return


widthMAX = 300
heightMAX = 300
widthMIN = -300
heightMIN = -300


turtle.setup(widthMAX*2,heightMAX*2)

head = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('red')
head.speed(0)
head.pensize(5)




while(True):
    head.forward(random.randint(1,4) * 10)
    if(random.randint(0, 100) > 50):
        head.left(random.randint(1, 4) * 90)
    else:
        head.right(random.randint(1, 4) * 90)
    keep()



 
turtle.done()




    
    
    