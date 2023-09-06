# Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma VOGAL ou o
# valor booleano False (falso) caso contrário.
# receber um string 
# identificar se é vogal
def eh_vogal(dado):
    vogais='aeiou'
    if(dado in vogais):
        return True
    else:
        return False

def main():
    receber_dados = input()
    receber_dados = receber_dados.lower()
    print(eh_vogal(receber_dados))
if (__name__ == '__main__'):
    main()

