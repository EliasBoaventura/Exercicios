# prova de matematica básica

def gabarito(reposta_correta, reposta_usuario):
    if(reposta_correta == reposta_usuario):
        print('Resposta correta')
        return 1    
    else:
        print('Resposta incorreta! Resposta certa é ' + reposta_correta)

def main():
    score = 0
    print('Prova de matematica básica. Nota máxima 5')
    questao_um = input('Qual resultado da expressão 3 + 4: ').strip().lower() 
    if(gabarito('7',questao_um)):
        score+=1
    questao_um = input('Qual resultado da expressão 10 - 4: ').strip().lower() 
    if(gabarito('6',questao_um)):
        score+=1
    questao_um = input('Qual resultado da expressão 7 x 4: ').strip().lower() 
    if(gabarito('28',questao_um)):
        score+=1
    questao_um = input('Qual resultado da expressão 8 / 4: ').strip().lower() 
    if(gabarito('2',questao_um)):
        score+=1
    questao_um = input('Qual resultado da expressão 4 % 2: ').strip().lower() 
    if(gabarito('0',questao_um)):
        score+=1
    
    print('Prova finalizada o seu seultado foi: ' + str(score))

if __name__=='__main__':
    main()