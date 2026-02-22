import turtle
import math

cart = 400
td = turtle.Turtle()

def drawcart():
    td.hideturtle()
    td.speed(0)

    td.down()
    td.right(90)
    td.forward(cart)
    td.forward(-2*cart)
    td.forward(cart)
    td.right(90)
    td.forward(2*cart)
    td.forward(-4*cart)
    td.forward(2*cart)
    td.right(180)
    td.right(1)


td.speed(10)

scale = 80
def radiusCalculation(angle):
    angle = rads(angle)
    heart = scale*(3.5-1.5*abs(math.cos((angle)))*math.sqrt(1.3+abs(math.sin((angle))))+math.cos(2*(angle))-3*math.sin((angle))+0.7*math.cos(12.2*(angle)))
    head = scale * (math.sin((math.pow(2,(angle))))-1.7)
    test = scale * math.atan(5*angle/4)
    return heart
def rads(ang):
    return math.radians(ang)
drawcart()
yoffset = 40
step = 1
rotationsneeded = 5
td.up()
for degree in range(0,360*rotationsneeded,step):
    td.goto(radiusCalculation(degree)*math.cos(math.radians(degree)),yoffset+radiusCalculation(degree)*math.sin(math.radians(degree)))
    td.down()
turtle.exitonclick()
