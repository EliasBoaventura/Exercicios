
def fatorial(numero):
    resultado = numero
    fatorial = 0
    if numero == 0 : return 1

    for i in range(1, (numero - 1)):
        fatorial = resultado * (numero - 1)
        resultado = fatorial
        numero -= 1

    return fatorial


def main():
    numero = input()
    numero = int(numero)


    resultado = fatorial(numero)
    
    print(resultado)
if __name__ == '__main__':
    main()