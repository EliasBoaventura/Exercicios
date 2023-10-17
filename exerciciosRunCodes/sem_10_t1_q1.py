#01. Escreva um programa que mostre todos os números inteiros de 1 a 50 (um por linha).


def ler_numero(quantidade):
    for i in range(quantidade):
        print(f'{i + 1}')

def main():
    quantidade = 50
    ler_numero(quantidade)    

if __name__ == '__main__':
    main()