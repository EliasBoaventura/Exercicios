from turtle import *

shape('turtle')
speed(7)

for i in range(5):
    forward(90)
    right(72)

penup()
right(90)
forward(180)
pendown()

for i in range(6):
    forward(90)
    right(60)

penup()
left(90)
forward(180)
pendown()

pensize(10)
for i in range(360):
    forward(1)
    right(1)
done() 