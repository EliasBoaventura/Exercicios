from turtle import *
from random import *

def muda_posicao_desenho():
    penup()
    setpos(randint(-400,400), randint(-400,400))
    pendown()

def criar_estrela(cor):
    tamanho = randrange(10,80)
    color(cor)
    pendown()
    begin_fill()
    for i in range(4):
        left(144)
        forward(tamanho)
    end_fill()    
    penup()


bgcolor("MidnightBlue")

for estrelas in range(randrange(0,20)):

    criar_estrela('white')
    muda_posicao_desenho()