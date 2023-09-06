# Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma CONSOANTE
# ou o valor booleano False (falso) caso contrário.
# ler um caractere
# verificar se é consoante


def eh_consoante(caractere):

    consoantes = 'bcdfgjklmnpqrstvwxz'
    if (caractere in consoantes):
        return True
    else:
        return False       

def main():
    ler_caractere = input()
    
    print(eh_consoante(ler_caractere.lower()))
if (__name__ == '__main__'):
    main()  