import turtle, random

image = turtle.Screen()
pencil = turtle.Turtle()


image.bgcolor("black")
pencil.color("white")
pencil.speed(0)



for n in range(1000):
    pencil.color('#%02X%02X%02X' % (255,n%256,0))    
    pencil.circle(20+n/16)
    pencil.right(10)
    pencil.forward(0 + n/16)
pencil.goto(0,0)
for n in range(1000):
    pencil.color('#%02X%02X%02X' % (0,0,n%256))    
    pencil.circle(20+n/16)
    pencil.right(10)
    pencil.forward(1 + n/16)

turtle.done()