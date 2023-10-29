def soma_numeros():
    soma = 0
    while(True):
        numero = int(input())
        if(numero == 0):
            break
        soma += numero
    return soma


def main():
    resultado = soma_numeros()

    print(resultado)


if __name__=='__main__':
    main()