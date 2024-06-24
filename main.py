"""
---------------------------------------
    * Course: 100 Days of Code - Dra. Angela Yu
    * Author: Noah Louvet
    * Day: 18 - Spirograph
    * Subject: Tkinter GUI
---------------------------------------
"""

import turtle
from turtle import Turtle, Screen
from random import choice, randint
#import turtle as t

tim = Turtle()
tim.shape("turtle")
tim.color("red")
turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


screen = Screen()
heading = [0, 90, 180, 270]
tim.speed("fastest")

tim.width(2)
angle = 0


def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):

        tim.pencolor(random_color())
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(150)

draw_spirograph(10)

screen.exitonclick()
