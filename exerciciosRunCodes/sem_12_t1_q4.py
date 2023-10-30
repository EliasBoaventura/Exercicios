
def calcula_numero_da_sorte(data):
    numero_da_sorte = 0
    
    while(data):
        numero_da_sorte += data % 10
        data = data // 10

    return numero_da_sorte


def main():
    data_de_nascimento = input()
    data_de_nascimento = int(data_de_nascimento)

    resultado = calcula_numero_da_sorte(data_de_nascimento)
    
    print(resultado)

if __name__ == '__main__':
    main()