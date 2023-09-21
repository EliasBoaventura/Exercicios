# 03. Escreva um programa que leia um número inteiro entre 10 e 99, mostre uma das mensagens, a seguir, conforme o
# número lido.
# • Nenhum dígito é ímpar.
# • Apenas um dígito é ímpar.
# • Os dois dígitos são ímpares.
def quantos_numeros_impares(numero):
    quantidade_numeros_impares = 0
    posicao_zero = numero[0]
    posicao_um = numero[1]
    
    if(int(posicao_zero)%2!=0): 
        quantidade_numeros_impares+=1
    if(int(posicao_um)%2!=0): 
        quantidade_numeros_impares+=1
        
    return quantidade_numeros_impares

def mostrar_quantos_impares(numero):
    status = ''
    if(quantos_numeros_impares(numero) == 0):
        status = 'Nenhum dígito é ímpar.'
    if(quantos_numeros_impares(numero) == 1):
        status = 'Apenas um dígito é ímpar.'
    if(quantos_numeros_impares(numero) == 2):
        status = 'Os dois dígitos são ímpares.'
    return status      

def main():
   numero = input()

   if(len(numero) == 2):
        print(mostrar_quantos_impares(numero))
   elif(True):
        print(0)

if __name__=='__main__':
    main()