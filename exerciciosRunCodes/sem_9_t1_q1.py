# 01. Escreva um programa que leia 3 (três) números inteiros e escreva uma das mensagens abaixo, de acordo com os
# valores lidos:

# • Todos os valores são diferentes;
# • Existem dois valores iguais e um diferente;
# • Todos os valores são iguais.

def classifica_valores(primeiro_valor, segundo_valor, terceiro_valor):
    frase = ''
    if(primeiro_valor == segundo_valor == terceiro_valor):
        frase = 'Todos os valores são iguais'

    elif((primeiro_valor == segundo_valor != terceiro_valor) or (primeiro_valor == terceiro_valor != segundo_valor) or 
         (segundo_valor == terceiro_valor != primeiro_valor)):
        frase = 'Existem dois valores iguais e um diferente'

    elif(primeiro_valor != segundo_valor != terceiro_valor):
        frase = 'Todos os valores são diferentes'
    else:
        raise ValueError('Entrada de dados incorreta ou não aceito as condições para retornar a frase')    
    
    return frase    

def main():
    valor_um = input()
    valor_dois = input()
    valor_tres = input()

    valor_um = int(valor_um)
    valor_dois = int(valor_dois)
    valor_tres = int(valor_tres)

    resultado = classifica_valores(valor_um, valor_dois, valor_tres)
    print(f'{resultado}')

if __name__ == '__main__':
    main()