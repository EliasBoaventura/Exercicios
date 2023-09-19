# 04. Escreva um programa que leia um caractere e mostra uma das mensagens: “vogal”, “consoante”, “número” ou
# “símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e outros como “símbolo”.
import string

# verifica se é vogal
def vogal(caractere):
    if(caractere in 'aeiou'):
        return True
    else:
        return False
#verifica se é consoante 
def consoante(caractere):
    alfabeto = list(string.ascii_lowercase)#cria uma lista do alfabeto em minusculo
    #se a variável caractere nao for vogal e estiver em alfabeto ela é uma consoante
    if(not vogal(caractere) and caractere in alfabeto):
        return True
    else:
        return False
    #verifica se é um número
def e_numero(caractere): 
    if(caractere in '0123456789'):
        return True
    else:
        return False
    #função que verifica as funções secundarias
def define_caractere(caractere):
    definicao = None
    if(vogal(caractere)):
        definicao = 'vogal'
    elif(consoante(caractere)):
        definicao = 'consoante'
    elif(e_numero(caractere)):
        definicao = 'número'
    elif(not vogal(caractere) or not consoante(caractere) or not e_numero(caractere)):
        definicao = 'símbolo'
    else:
        return print('Entrada inválida')   
    return definicao    

def main():
    caractere = input().lower()
    print(define_caractere(caractere))

if __name__=='__main__':
    main()