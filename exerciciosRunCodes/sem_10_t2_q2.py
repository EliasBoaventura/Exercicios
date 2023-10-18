def main():
    for i in range(99, 251):
        resultado = f'{i} bugs no software, pegue um deles e conserte...'
        print(resultado)
        print('Tecle "Ctrl+F5"')
        if i == 250:
            print(('Vamos fazer mais um café!'))

if __name__ == '__main__':
    main()