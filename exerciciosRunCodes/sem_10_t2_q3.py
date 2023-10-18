def main():
    memoria = 0
    for i in range(99, 251):
        if(i == 99 or memoria == i):
            resultado = f'{i} bugs no software, pegue sete deles e conserte...'
            print(resultado)
            print('Tecle "Ctrl+F5"')
            memoria = i + 7
    
    print(('Vamos fazer mais um café!'))
        

if __name__ == '__main__':
    main()