from turtle import *
from time import *

bgcolor("black")
t = [Turtle(), Turtle()]
x = 6
colors=["red","yellow","blue","lime",]
for index, i in enumerate(t):
    i.speed(0)
    i.color("white")
    i.shape("circe")
    i.shapesize(0.3)
    i.width(3)
    i.pu()
    i.seth(90)
    i.fd(350)
    i.seth(-180)
    i.pd()
t[0].pu()
    