from turtle import Turtle

tim = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

for _ in range(15):
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.forward(10)

