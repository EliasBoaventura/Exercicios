
def main():
    valor_compra = input().strip()
    valor_compra = int(valor_compra)
    
    for i in range(1, 25):
        resultado = valor_compra/i
        print(f'{i}x de R$ {resultado:.2f}')


if __name__ == '__main__':
    main()