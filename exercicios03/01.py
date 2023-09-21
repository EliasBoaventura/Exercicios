# criando um jogo simples com if e else



def main():
    print('Iae bruxo? Responda essa pergunta e entrará no game.')
    print('Um cubo mágico tem quantos lados?')

    resposta = input().strip().lower()

    if(resposta == 'varios'):
        print('parabéns, voce é um bruxo!!!')
    else:
        print('Voce é um trouxa')
    print('-'*30)
    print('obrigado por jogar!!!')
if __name__ == '__main__':
    main()
