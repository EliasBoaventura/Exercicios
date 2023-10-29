def inverte_numero(numero):
    return numero[::-1]


def main():
    numero = input().strip()
    
    resultado = inverte_numero(numero)
    print(int(resultado))
    
if __name__=='__main__':
    main()