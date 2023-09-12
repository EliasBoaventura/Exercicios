# 05. Você é dono de uma loja que vende roupas. Sua política é de dar desconto para quem compra à vista, vender pelo preço de
# etiqueta para quem paga em 5 vezes e cobrar jutos de quem comprar em 10 vezes. Escreva um programa que leia o valor de
# uma compra e imprima três valores, todos com até duas casas decimais:
# • Valor para pagamento à vista, com desconto de 9%.
# • Valor da prestação para pagamento em 5 vezes, sem desconto nem juros.
# • Valor da prestação para pagamento em 10 vezes, com 17% de juros.



def valor_com_desconto_a_vista(valor):
    valor = valor - (valor * 9/100)
    return valor

def valor_pagamento_em_cinco_vezes(valor):
    valor_da_prestacao = (valor / 5)
    return valor_da_prestacao

def valor_pagamento_em_dez_com_juros(valor):
    valor = valor + (valor * 17/100)
    valor_da_parcela = (valor / 10)
    return valor_da_parcela

def main():
    valor_compra = input()
    valor_compra = float(valor_compra)

    print(f'{valor_com_desconto_a_vista(valor_compra):.2f}')
    print(f'{valor_pagamento_em_cinco_vezes(valor_compra):.2f}')
    print(f'{valor_pagamento_em_dez_com_juros(valor_compra):.2f}')

if __name__ == '__main__':
    main()    