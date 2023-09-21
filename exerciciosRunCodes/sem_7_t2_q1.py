# Escreva um programa que leia o nome e o estado civil de uma pessoa, considere apenas “1” para casado e “2” para
# solteiro. Se a pessoa for casada, leia, também, o nome do cônjuge. Mostre quantos caracteres no total existem no(s)
# nome(s) lido(s).

def e_casado(estado_civil):
    if(estado_civil == 1):
        return True
    elif(estado_civil == 2):
        return False
    else:
        print('Entrada de dados incorreta')


def main():
    nome = input().strip()
    estado_civil = input()

    estado_civil = int(estado_civil)
    
    if(e_casado(estado_civil)):
        nome_conjuge = input().strip()
        print(len(nome_conjuge) + len(nome))
    elif(not e_casado(estado_civil)):
        print(len(nome))

if __name__=='__main__':
    main()