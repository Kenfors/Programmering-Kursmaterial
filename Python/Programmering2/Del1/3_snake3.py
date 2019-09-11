import turtle, random

def keep():
    angle = head.towards(0,0)
    angle += 22
    angle -= (angle%45)
    head.setheading(angle)
    return
    
def randomColor():
    newcolor = random.choice(COLORS)
    head.pencolor(newcolor)
    head.fillcolor(newcolor)


widthMAX = 300
heightMAX = 300
widthMIN = -300
heightMIN = -300

COLORS = [
    "yellow",
    "green",
    "red",
    "blue",
    "purple",
    "orange",
    "pink",
    "lightgreen",
    "lightblue"
]

turtle.setup(widthMAX*2,heightMAX*2)

head = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
head.pencolor('green')
head.fillcolor('green')
head.speed(0)
head.pensize(5)



iterations = 0
head.begin_fill()
while(True):
    head.forward(random.randint(1,3) * 70)

    keep()
    if(random.randint(0, 100) > 50):
        head.left(random.randint(-3, 3) * 30)
    else:
        head.right(random.randint(-3, 3) * 30)
    if(iterations >= 2):
        head.end_fill()
        head.begin_fill()
        randomColor()
        iterations = 0
    iterations+=1



 
turtle.done()




    
    
    