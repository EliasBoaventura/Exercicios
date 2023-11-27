
def contador(lista, valor):
    contador = 0
    for i in lista:
        if i == valor:
            contador += 1
    return contador


def cria_lista():
    lista = []
    while True:
        numeros = int(input())
        if numeros == 0:
            break
        lista.append(numeros)

    return lista


def main():
    lista = cria_lista()
    valor = int(input())
    resultado = contador(lista, valor)

    print(f'{lista}\n{valor}\n{resultado}')


if __name__ == "__main__":
    main()
