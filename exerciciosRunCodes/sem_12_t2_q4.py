
def e_primo(numero):
    for i in range(2, numero):
        if numero % i == 0: return False
    return True


def main():
    numero = input().strip()
    numero = int(numero)

    resultado = e_primo(numero)
    print(resultado)
    
if __name__ == '__main__':
    main()