def juros_composto(deposito, taxa_de_juros):
    valor_em_dobro = 2 * deposito
    quantidade_anos = 0
    while(deposito < valor_em_dobro):
        deposito += deposito * taxa_de_juros/100
        quantidade_anos+=1
    return quantidade_anos


def main():
    deposito_inicial = input()
    taxa_de_juros = input()
    deposito_inicial = float(deposito_inicial)
    taxa_de_juros = float(taxa_de_juros)

    resultado = juros_composto(deposito_inicial, taxa_de_juros)
    print(f'{resultado}')

if __name__=='__main__':
    main()