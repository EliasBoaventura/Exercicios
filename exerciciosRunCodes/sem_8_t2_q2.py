# 02. Escreva um programa que leia um número inteiro. Mostre a soma dos dígitos se o valor lido for entre 0 (zero) e
# 100 mil ou -1 (menos um) para outros valores. Exemplo: 12.476 deve mostrar a 20.


def soma_numeros(numero):
    tamanho = len(numero)
    soma = 0

    while(tamanho):
        soma += int(numero[tamanho - 1])
        tamanho -= 1 
    
    return soma


def main():
    numero = input().strip()

    if(0 <= int(numero) < 100000):
        resultado = soma_numeros(numero)
        print(resultado)
    else:
        print('-1')

if __name__ == '__main__':
    main()

