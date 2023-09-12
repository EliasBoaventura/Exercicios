# 01. Você sabia que os computadores amam contar coisas? Eles são como pequenos nerds! Vamos fazer um contador
# de letras. Peça ao usuário para digitar uma frase qualquer e, em seguida, imprima o número de caracteres nessa
# frase sem considerar espaços em branco no início ou final da frase digitada.

def leitor_caractere(frase):
    return len(frase)


def main():
    frase = input().strip()
    print(leitor_caractere(frase))


if __name__ == '__main__':
    main()    