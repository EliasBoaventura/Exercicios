# cada ano ¨6% dos vivos morrem 
# nascidos sao 1% da população inicial 

def controle_populacao(populacao):

    risco_de_extincao = populacao * 0.10
    populacao_nascida = 0
    populacao_morta = 0
    ano = 1600
    while(populacao >= risco_de_extincao):
        populacao_nascida = populacao * 0.01
        populacao_morta = populacao * 0.06
        
        populacao -= populacao * 0.05

        
        print(ano, round(populacao_nascida), round(populacao_morta), round(populacao), sep=',')
        ano += 1



def main():
    populacao_aves = input()
    populacao_aves = int(populacao_aves)

    controle_populacao(populacao_aves)



if __name__ == '__main__':
    main()