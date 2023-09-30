# 04. Escreva um programa que leia a altura e o sexo de uma pessoa, considere 1 para ‘homens’ e 2 para ‘mulheres’.
# Considerando duas casas decimais, calcule e mostre o peso ideal utilizando as seguintes fórmulas:
# • para homens: (72.7 * altura) – 58
# • para mulheres: (62.1 * altura) – 44.7



def qual_sexo(sexo):
    if(sexo==2):
        return 'mulheres'
    else:
        return 'homens'

def calcula_algo(altura, sexo):
    resultado = 0
    if(qual_sexo(sexo)=='homens'):
        resultado = (72.7 * altura) - 58
    elif(qual_sexo(sexo)=='mulheres'):
        resultado = (62.1 * altura) - 44.7
    else:
        raise ValueError('Entrada inválida')
    return resultado

def main():
    altura = input()
    sexo = input()
    altura = float(altura)
    sexo = int(sexo)

    resultado = calcula_algo(altura, sexo)

    print(f'{resultado:.2f}')


if __name__ == '__main__':
    main()