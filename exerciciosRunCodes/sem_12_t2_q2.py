

def fibonacci(numero):
    começo_fibonacci = 0
    memoria = 0
    proximo_valor_fibonacci = 1
    lista_fibonacci = []
    for i in range(numero):
        lista_fibonacci.insert(i, começo_fibonacci)
        memoria = começo_fibonacci
        começo_fibonacci += proximo_valor_fibonacci
        proximo_valor_fibonacci = memoria
    return lista_fibonacci
def main():
    numero = input()
    numero = int(numero)

    resultado = fibonacci(numero)
    print(str(resultado).replace('[', '').replace(']',''))
    
    

if __name__ == '__main__':
    main()