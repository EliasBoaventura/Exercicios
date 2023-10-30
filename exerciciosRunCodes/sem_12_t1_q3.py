

def calcula_tempo_ultrapassar_populacao(populacao_um, populacao_dois, natalidade_um, natalidade_dois):
    total_de_anos = 0
    memoria_polucao = populacao_um
    # memoria_natalidade = natalidade_um
    if(populacao_um < populacao_dois):
        populacao_um = populacao_dois
        populacao_dois = memoria_polucao
        # natalidade_um = natalidade_dois
        # natalidade_dois = memoria_natalidade

    while(populacao_um > populacao_dois):
        populacao_dois += populacao_dois * natalidade_dois/100
        populacao_um += populacao_um * natalidade_um/100
        total_de_anos += 1

    return total_de_anos

def main():
    populacao_pais_a = input()
    populacao_pais_b = input()

    populacao_pais_a = int(populacao_pais_a)
    populacao_pais_b = int(populacao_pais_b)
    taxa_natalidade_a = 2
    taxa_natalidade_b = 3

    resultado = calcula_tempo_ultrapassar_populacao(populacao_pais_a, populacao_pais_b, taxa_natalidade_a, taxa_natalidade_b)
    
    print(resultado)

if __name__ == '__main__':
    main()