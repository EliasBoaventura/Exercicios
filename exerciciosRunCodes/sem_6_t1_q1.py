#Escreva um programa que leia um nome pelo teclado e informe quantos caracteres o nome possui.
def main():
    nome = input()
    tamanho(nome)


def tamanho(nome):
    print(len(nome))

if (__name__== '__main__'):
    main()