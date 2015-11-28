import turtle
import time

def draw_recur_shapes(t,size,level):
    if level == 0:
        t.down()
        t.begin_fill()
        for i in range(3):
            t.forward(size)
            t.left(120)
        t.end_fill()
        t.up()

    else:
        for i in range(3):
            draw_recur_shapes(t,size/2,level-1)
            t.forward(size)
            t.left(120)
            print level

window = turtle.Screen()
window.bgcolor("white")
brad = turtle.Turtle()

brad.shape("turtle")
brad.color("green", "green")
brad.speed(1)
draw_recur_shapes(brad,200,3)

window.exitonclick()
