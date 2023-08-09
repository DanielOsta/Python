import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim.speed(speed="fastest")
for i in range(0, 360, 5):
    tim.color(random_color())
    tim.setheading(i)
    tim.circle(100)

turtle.exitonclick()
