#Escreva um programa que leia o nome e o sexo de uma pessoa, e mostre o nome precedido da mensagem “Ilmo Sr.”, 
#caso seja informado o sexo masculino, ou “Ilma Sra.” se for informado o sexo feminino. Use o número inteiro 1 
#para identificar masculino e 2 para identificar feminino.

def qual_sexo(sexo, nome):
    if(sexo == 1):
        print(f'Ilmo Sr. {nome}')

    elif(sexo == 2):
        print(f'Ilma Sra. {nome}')

    else:
        return 'Entrada inválida'    
def main():
    nome = input().strip()
    sexo = input()
    sexo = int(sexo)

    qual_sexo(sexo, nome)
if __name__=='__main__':
    main()


