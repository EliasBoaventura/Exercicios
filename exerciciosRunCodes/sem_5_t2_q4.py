# Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogal
# ou consoante) ou um NÚMERO (entre ‘0’ e ‘9’) ou valor booleano False (falso) caso contrário.

def eh_letra(dado):
    alfa_Numerico = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    if(dado in alfa_Numerico):
        return True
    else:
        return False

def main():
    receber_dados = input()
    
    print(eh_letra(receber_dados.upper()))
if (__name__ == '__main__'):
    main()
