# Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for um SÍMBOLO (o
# que não é letra ou número) ou o valor booleano False (falso) caso contrário.

def eh_letra(dado):
    alfa_Numerico = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    if(dado in alfa_Numerico):
        return False
    else:
        return True

def main():
    receber_dados = input()
    
    print(eh_letra(receber_dados.upper()))
if (__name__ == '__main__'):
    main()
