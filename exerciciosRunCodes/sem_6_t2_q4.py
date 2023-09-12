# 04. Um alienígena chamado Zob precisa de ajuda para converter anos terrestres em anos espaciais! Sabendo que 1 ano
# terrestre equivale a meio ano espacial, calcule e imprima uma idade inserida pelo usuário em anos espaciais.




def idade_espacial(idade_terrestre):
    idade_espacial = idade_terrestre / 2
    return round(idade_espacial,2)

def main():
    idade = input()
    idade = int(idade)

    print(f'{int(idade_espacial(idade))}')


if __name__ == '__main__':
    main()    