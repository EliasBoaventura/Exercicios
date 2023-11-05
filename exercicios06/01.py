from turtle import *

def desenha_quadrado():
    pendown()
    begin_fill()
    
    for i in range(3):
        left(90)
        forward(100)
    end_fill()
    penup()


color("whiteSmoke")
bgcolor("black")

desenha_quadrado()
forward(200)
desenha_quadrado()
forward(200)
desenha_quadrado()

hideturtle()
done()
