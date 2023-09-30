# 01. Escreva um programa que leia um número inteiro e some 5 caso valor lido seja par ou some 8 caso o valor lido seja
# ímpar. Mostre na tela o resultado da operação.

def eh_par(numero):
    return numero % 2 == 0

def main():
    numero = input()
    numero = int(numero)    

    if(eh_par(numero)):
        numero +=5
    else:
        numero +=8

    print(numero)    


if __name__ == '__main__':
    main()