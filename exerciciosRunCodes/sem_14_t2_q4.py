def cria_lista():
    lista = []
    for i in range(5):
        numeros = int(input())
        lista.append(numeros)
    return lista


def produto_escalar(lista_um, lista_dois):

    produto = 0

    for i in range(5):
        produto += lista_um[i] * lista_dois[i]

    return produto


def main():
    lista1 = cria_lista()
    lista2 = cria_lista()

    resultado = produto_escalar(lista1, lista2)

    print(f'{lista1}\n{lista2}')
    print(f'({lista1[0]} x {lista2[0]}) + ({lista1[1]} x {lista2[1]}) + ({lista1[2]} x {lista2[2]}) + ({lista1[3]} x {lista2[3]}) + ({lista1[4]} x {lista2[4]}) = {resultado}')

if __name__ == "__main__":
    main()
