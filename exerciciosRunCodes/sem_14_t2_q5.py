def cria_lista():
    lista = []
    for i in range(10):
        numeros = int(input())
        lista.append(numeros)
    return lista


def uniao_listas_sem_repetidos(lista_um, lista_dois):
    lista_unida_sem_repeticao = []
    lista_unida = []

    for i in range(10):
        lista_unida.append(lista_um[i])

    for i in range(10):

        lista_unida.append(lista_dois[i])

    for y in lista_unida:
        if y not in lista_unida_sem_repeticao:
            lista_unida_sem_repeticao.append(y)

    return lista_unida_sem_repeticao


def main():
    lista_um = cria_lista()
    lista_dois = cria_lista()

    resultado = uniao_listas_sem_repetidos(lista_um, lista_dois)
    print(resultado)


if __name__ == "__main__":
    main()
