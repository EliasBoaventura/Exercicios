# 05. Escreva um programa que leia três números inteiros correspondentes a três notas de um aluno. Apresente a média
# das três notas, mas, se a terceira nota for superior a 8, o aluno deve ganhar mais um ponto na média. Além disso,
# se a média final, em função do ponto extra, ficar acima de 10 ela deve ser ajustada para 10.

def media(nota_um, nota_dois, nota_tres):
    media = (nota_um + nota_dois + nota_tres)/3
    
    if(nota_tres > 8):
        media += 1
    if(media > 10):
        media = 10
    return media

def main():
    nota_um = input()
    nota_dois = input()
    nota_tres = input()

    nota_um = float(nota_um)
    nota_dois = float(nota_dois)
    nota_tres = float(nota_tres)

    print(f'{(media(nota_um, nota_dois, nota_tres))}')

if __name__=='__main__':
    main()