from turtle import *



def drawPlanet(cor, tamanho):
    color(cor)
    penup()
    left(90)
    forward(150)
    pendown()
    begin_fill()
    for i in range(1,360):
        forward(tamanho)
        right(1)
    end_fill()
shape("turtle")
speed(7)
bgcolor("black")
drawPlanet("white", 2)

hideturtle()
done()