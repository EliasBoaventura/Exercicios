#02. Escreva um programa que leia o um conjunto de 100 números inteiros positivos e determine a quantidade
#de números pares e números ímpares contidos no mesmo.
def e_par(numero):
    return numero % 2 == 0

def main():
    quantidade_numeros_pares = 0
    quantidade_numeros_impares  = 0
    for i in range(100):
        numero = input().strip()
        numero = int(numero)
        if(e_par(numero)):
            quantidade_numeros_pares += 1
        if(not e_par(numero)):
            quantidade_numeros_impares += 1    
    print(f'{quantidade_numeros_pares}\n{quantidade_numeros_impares}')


if __name__ == '__main__':
    main()