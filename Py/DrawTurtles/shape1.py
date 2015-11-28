import turtle
import time

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(0)

    for n in range(360/10):
        for i in range(2):
            brad.forward(100)
            brad.right(45)
            brad.forward(100)
            brad.right(135)
        brad.right(10)

    brad.right(90)
    brad.forward(300)
    window.exitonclick()

draw_flower()
