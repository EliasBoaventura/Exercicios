# 03. Escreva um programa que leia um conjunto de 100 números inteiros e exiba o valor médio dos mesmos
# (com duas casas decimais).
def media(soma, quantidade):
    return soma/quantidade

def main():
    quantidade = 100
    soma = 0

    for i in range(quantidade):
        numero = int(input())
        soma += numero
        

    resultado = media(soma, quantidade)
    print(f'{resultado:.2f}')

if __name__ == '__main__':
    main()
