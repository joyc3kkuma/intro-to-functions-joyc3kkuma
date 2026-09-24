import turtle
from turtle import *
t = Turtle()

t.shape('turtle') 

""" def square(x,y):
    t.forward(x)
    t.left(y)
    sidelength = 100
    rotate = 90

def triangle(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
triangle(100,90)

def sixtySquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length = length + 5
        t.left(5)
        sixtySquares(60)  """

def star(x,y):
    for i in range(5):
        t.forward(x)
        t.left(y)
def star_loop(iRange):
    length = 5
    for i in range(iRange):
        star(length, 144)
        length = length + 5
        t.left(5)
star_loop(60)


turtle.done()