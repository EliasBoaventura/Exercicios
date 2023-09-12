# 03. Você foi ao mercado mágico e, ao comprar 3 maçãs e 2 bananas, o caixa precisa da sua ajuda para calcular o total!
# Leia o preço de uma maçã e o preço de uma banana, calcule e imprima o total da sua compra.


def total_compra(preco_maca, quantidade_maca, preco_banana, quantidade_banana):
    total_value = (preco_maca * quantidade_maca) + (preco_banana * quantidade_banana)
    return round(total_value,2)

def main():
    preco_maca = input().strip()
    preco_banana = input().strip()
    quantidade_maca = 3
    quantidade_banana = 2

    preco_maca = float(preco_maca)
    preco_banana = float(preco_banana)
    
    print(f'{total_compra(preco_maca, quantidade_maca, preco_banana, quantidade_banana):.2f}')


if __name__ == '__main__':
    main()    