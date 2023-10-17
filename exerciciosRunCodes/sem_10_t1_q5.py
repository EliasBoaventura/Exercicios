 #05. Escreva um programa que leia um conjunto de 100 números inteiros positivos e determine o maior deles.

def main():
    resultado =[]
    for i in range(100):
        numero = int(input())
        resultado.insert(i,numero)
    print(max(resultado))

if __name__ == '__main__':
    main()