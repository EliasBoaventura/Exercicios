# Escreva um programa que leia um único caractere pelo teclado e informe o código numérico correspondente ao caractere lido.

def codigo_numerico(caractere):
    return ord(caractere)


def main():
    caractere = input()
    print(codigo_numerico(caractere))


if (__name__=='__main__'):
    main()    