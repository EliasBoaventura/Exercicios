
def media_aritmetica(soma_valores, quantidade):
    return soma_valores / quantidade

def main():
    soma = 0
    quantidade_numero_lidos  = 0
    while True:
        numero = int(input())
        if numero == 0:
            break
        soma += numero
        quantidade_numero_lidos += 1    

    resultado = media_aritmetica(soma, quantidade_numero_lidos)
    print(f'{resultado:.2f}')
if __name__=='__main__':
    main()