#Escreva um programa/algoritmo que leia 5 (cinco) números inteiros e escreva na tela:
#• o maior número lido;
#• o menor número lido;
#• a média aritmética dos números lidos.


def ler_numeros(quantidade_numeros, lista_numeros):
    condicao = 0 
    while(condicao < quantidade_numeros):
        numero = int(input())
        
        lista_numeros.insert(condicao, numero)
        condicao += 1
    return lista_numeros 
      

def maior_numero(numeros):
    return max(numeros)

def menor_numero(numeros):
    return min(numeros)

def media(lista, quantidade):
    contador = 0
    soma = 0
    while(contador < quantidade):
        soma += lista[contador]

        contador+=1
    media = (soma/quantidade)   
    return media

def main():
    quantidade_numeros = 5
    lista = []
    
    ler_numeros(quantidade_numeros, lista)
    print(maior_numero(lista))
    print(menor_numero(lista))
    print(media(lista, quantidade_numeros))

if __name__ == '__main__':
    main()