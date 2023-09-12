# 02. Nem sempre as transações financeiras resultam em números inteiros. Vamos usar o round() para resolver isso!
# Peça ao usuário para inserir uma quantidade de dinheiro. Em seguida, arredonde esse valor para o número inteiro
# mais próximo e imprima o resultado.


def arredondar_valor(dinheiro):
    return round(dinheiro)


def main():
    dinheiro = input()
    dinheiro = float(dinheiro)
    print(arredondar_valor(dinheiro))


if __name__ == '__main__':
    main()    