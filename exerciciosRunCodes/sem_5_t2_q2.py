# Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogal
# ou consoante) ou o valor booleano False (falso) caso contrário.
# ler um caracter
# verificar se é letra ou numero

def eh_letra(dado):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if(dado in alfabeto):
        return True
    else:
        return False

def main():
    receber_dados = input()
    
    print(eh_letra(receber_dados.upper()))
if (__name__ == '__main__'):
    main()
