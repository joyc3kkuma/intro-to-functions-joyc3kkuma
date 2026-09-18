import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

def square(x,y):
    for i in range(60):
        t.forward(x+5)
        t.left(y+5)
square(100,90)

def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 5
doubleSquares(5)

turtle.done()

