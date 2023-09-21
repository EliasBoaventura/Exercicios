#Escreva um programa que leia três números por parâmetro e mostre na tela em ordem crescente.


def ordem_crecente(numero_um, numero_dois, numero_tres):
    intermediario = 0
    menor = min(numero_um, numero_dois, numero_tres)
    maior = max(numero_um, numero_dois, numero_tres)

    # ja tenho o maior e o menor de 3 numeros como faco pra saber o numero entre eles?
    # cria uma lista e remover os que voce ja sabe

    exemplo_lista = [numero_um, numero_dois, numero_tres]
    if(menor in exemplo_lista):
        exemplo_lista.remove(menor)
    if(maior in exemplo_lista):
        exemplo_lista.remove(maior)
    intermediario = exemplo_lista[0]

    return menor, intermediario, maior
   

def main():
    numero_um = input()
    numero_dois = input()
    numero_tres = input()

    numero_um = int(numero_um)
    numero_dois = int(numero_dois)
    numero_tres = int(numero_tres)

    menor, intermediario, maior = ordem_crecente(numero_um, numero_dois, numero_tres)
    print(f'{menor}\n{intermediario}\n{maior}')

if __name__=='__main__':
    main()