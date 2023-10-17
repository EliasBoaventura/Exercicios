#04. Escreva um programa que gere a seguinte sequência:
#10, 20, 30, 40, ..., 990, 1000.
#Considere a separação dos números por vírgula seguido de espaço em branco e o ponto no final da
#sequência.


def ler_numero(quantidade):
    for i in range(quantidade):
        if(i<99):    
            print(f'{i+1}0',end=', ')
        if(i == 99):
            print(f'{i+1}0',end='.')

def main():
    valor = 100

    ler_numero(valor)


if __name__ == "__main__":
    main()