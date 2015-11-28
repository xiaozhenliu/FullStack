import turtle
import time

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    for i in range(4):
        brad.forward(100)
        brad.right(90)
    time.sleep(10)
draw_square()
