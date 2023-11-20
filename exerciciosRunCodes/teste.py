lista = ['a','c','d']

memoria = lista[1]
if isinstance(memoria, str):
    if memoria.isnumeric():
        lista_ordenada = sorted(lista, key=float)
    else:
        lista_ordenada = sorted(lista)