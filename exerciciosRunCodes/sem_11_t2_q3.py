def tabela_opcoes():
    print('OPÇÕES:\n1 - SAUDAÇÃO\n2 - BRONCA\n3 - FELICITAÇÃO\n0 - FIM')

def tabela_reposta(numero):
    if(numero == 1):
        print('1 - Olá. Como vai?')
    elif(numero == 2):
        print('2 - Vamos estudar mais.')
    elif(numero == 3):
        print('3 - Meus Parabéns!')    
    elif(numero == 0):
        print('0 - Fim de serviço.')

def main():
    while True:
        tabela_opcoes()
        resposta_usuário = int(input())
        if(str(resposta_usuário) not in '0123'):
            print('Opção inválida.')
            continue    
        tabela_reposta(resposta_usuário)
        if(resposta_usuário == 0):
            break    

if __name__=='__main__':
    main()