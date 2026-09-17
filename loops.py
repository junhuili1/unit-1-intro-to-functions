import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(0)

def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)

def triangle():
    for i in range(3):
        t.forward(100)
        t.left(120)

def turningSquares():
    for i in range (60):
        for i in range(4):
            t.forward(100)
            t.left(90)
        t.right(5)

def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2

def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25

def spiralSquares(iRange):
    length = 5
    t.right(90)
    for i in range(iRange):
        square(length, 90)
        length += 5
        t.right(5)
# spiralSquares(60)

def star(x):
    for i in range(5):
        t.forward(x)
        t.right(144)

def spiralStars(iRange):
    length = 5
    for i in range(iRange):
        star(length)
        length += 5
        t.right(5)
spiralStars(60)

turtle.done()