# criando um quiz 


def main():
    print('Prova de matematica.')
    print('-' * 30)
    print('''Qual valor da área de um quadrado de lado 4?
    alternativas:
    a -> 2
    b -> 4
    c -> 8
    d -> 16''')
    print('Digite sua resposta:', end=' ')
    resposta = input().strip().lower()

    if(resposta == 'a'):
        print('meu fi pelo amor de Deus!!!')
    elif(resposta == 'b'):
        print('ERROOOOU')
    elif(resposta == 'c'):
        print('Ainda nao amigo') 
    elif(resposta == 'd'):
        print('Acertou mizeravi!!!')       
    else:
        print('essa alternativa nao existe')

    print('Boa prova.')

if __name__ == '__main__':
    main()
