
def calculo_h(numero):
    h = 0
    while numero:
        h += 1/(numero)
        numero -= 1
    return h

def main():
    n = input()
    n = int(n)

    resultado = calculo_h(n)
    print(f'{resultado:.4f}')


if __name__ == '__main__':
    main()