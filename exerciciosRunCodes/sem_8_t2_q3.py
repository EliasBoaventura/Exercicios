# 03. Escreva um programa que leia um número inteiro positivo e escreva na tela:

# • FIZZ se o número é divisível por três;
# • BUZZ se o número é divisível por cinco;
# • FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo.
# • O próprio número caso não seja divisível por três ou por cinco.
# OBS: para cada número lido apenas uma resposta deve ser impressa.



def fizz_buzz(numero):
    status = ''
    if(numero%3==0 and numero%5==0):
        status = 'FIZZBUZZ'        
    elif(numero%3==0):
        status = 'FIZZ'
    elif(numero%5==0):
        status = 'BUZZ'
    elif(not(numero%3==0 or numero%5==0)):
        status = str(numero)
    else:
        raise ValueError(f'entrada {numero} incorreta') 
    return status

def main():
    numero = input()
    numero = int(numero)
    resultado = fizz_buzz(numero)
    
    print(f'{resultado}')
    
    

if __name__ == '__main__':
    main()