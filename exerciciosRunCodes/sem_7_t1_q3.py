# 03. Escreva um programa que leia a cor de um sinal de trânsito (“V” é verde; “A” é amarelo; “E” é vermelho) e retorne
# a respectiva mensagem “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.

def semaforo(cor):
    status = None
    cor = str(cor).upper()
    
    if(cor == 'V'):
        status ='Siga'
    elif(cor == 'A'):
        status ='Atenção'
    elif(cor == 'E'):
        status ='Pare'
    else:
        status ='Entrada inválida'
    return status    

def main():
    cor_sinal = input()
    print(semaforo(cor_sinal))
   

if __name__=='__main__':
    main()