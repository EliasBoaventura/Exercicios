#escreva um programa que leia o tempo de duração de um evento em uma fábrica expresso em segundos. Calcule e exiba esse
#tempo em horas, minutos e segundos (HH:MM:SS)

def converte_Segundos(segundos):
    horas = 0
    minutos = 0
    segundos_restantes = 0
    if(segundos > 3600):
        horas = segundos//3600
        segundos = (segundos - (horas * 3600))

    if(segundos > 60):
        minutos = segundos//60
        segundos = segundos - (minutos * 60)

    if(segundos > 0):
        segundos_restantes = segundos

    print(f'{horas}:{minutos}:{segundos_restantes}')    

def main():
    segundos = int(input())
    converte_Segundos(segundos)

if __name__== '__main__':
    main()