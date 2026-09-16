import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

""" t.forward(200)
 """

def rectangle(x): 
    t.forward(x)
    t.left(125)
    t.forward(x)
    t.left(100)
    t.forward(x)
    t.left(125)
    t.forward(x)
    t.left(100)
rectangle(200)



turtle.done()