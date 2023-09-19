#Escreva um programa que leia um número e mostra o valor booleano True (verdadeiro) se o número for ímpar ou o 
# valor booleano False (falso) caso contrário.


def e_par(numero):
    if(numero % 2):
        return True
    else:
        return False
def main():
    numero = input()
    numero = int(numero)
    
    print(f'{e_par(numero)}')
    
if(__name__ == '__main__'):
    main()