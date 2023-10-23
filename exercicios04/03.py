from turtle import *

shape('turtle')
speed(6)


lados = 10
angulo = 360/lados

for i in range(lados):
    forward(40)
    right(angulo)

penup()
right(90)
forward(180)
pendown()
pencolor('blue')
pensize(6)


for i in range(10):
    forward(100)
    right(200)
    for i in range(lados):
        forward(40)
        right(angulo)

done()    