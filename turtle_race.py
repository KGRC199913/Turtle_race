from turtle import *
from random import randint


def draw_track():
    penup()
    speed(0)
    goto(-140, 140)
    for count in range(15):
        write(count, align='center')
        right(90)
        forward(10)
        pendown()
        for count2 in range(10):
            forward(10)
            penup()
            forward(10)
            pendown()
        penup()
        backward(210)
        left(90)
        forward(20)


def run(a):
    a.forward(randint(1, 5))


def initialize(obj, color, x, y):
    obj.color(color)
    obj.shape('turtle')
    obj.penup()
    obj.goto(x, y)
    obj.right(360)


draw_track()
red, blue, green, yellow = Turtle(), Turtle(), Turtle(), Turtle()
initialize(red, 'red', -160, 100)
initialize(blue, 'blue', -160, 70)
initialize(green, 'green', -160, 40)
initialize(yellow, 'yellow', -160, 10)
for turn in range(105):
    run(red); run(blue); run(green); run(yellow)
done()
