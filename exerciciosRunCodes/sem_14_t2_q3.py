def cria_lista():
    lista = []
    for i in range(20):
        numeros = int(input())
        lista.append(numeros)

    return lista
def elimina_repetidos(lista):
    lista_sem_repeticao = []

    for i in lista:
        if i not in lista_sem_repeticao:
            lista_sem_repeticao.append(i)

    return lista_sem_repeticao

def main():
    lista = cria_lista()
    lita_sem_repetidos = elimina_repetidos(lista)

    print(f'{lita_sem_repetidos}')
if __name__=="__main__":
    main()