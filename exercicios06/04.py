from turtle import *
from random import *


def cor_aleatoria():
    cores = ["#0000CD", "#00FF7F","#4B0082", "#A52A2A", "#B0E0E6"]

    return choice(cores)
def local_aleatorio_tela():
    penup()
    setpos(randint(-400,400), randint(-400,400))
    pendown()

def desenha_algo():
    pendown()
    color(cor_aleatoria())
    
    local_aleatorio_tela()
    begin_fill()
    tamanho = randrange(17, 25)
    for i in range(7):
        forward(tamanho)
        left(75)
    end_fill()
    
def main():
    bgcolor("black")
    speed(7)
    for i in range(randrange(100,150)):
        desenha_algo()

    done()

if __name__ == "__main__":
    main()    
