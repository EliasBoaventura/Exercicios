def calcula_alcance_lebre(distancia):
    distancia_lebre = 0
    contador_tempo_alcance_em_minutos = 0
    while(distancia_lebre < distancia):
        distancia += 1
        distancia_lebre += 10
        contador_tempo_alcance_em_minutos += 1
    return contador_tempo_alcance_em_minutos

def main():
    vantagem_metros_tartaruga = input().strip()
    vantagem_metros_tartaruga = int(vantagem_metros_tartaruga)

    resultado = calcula_alcance_lebre(vantagem_metros_tartaruga)
    print(resultado)
    

if __name__ == '__main__':
    main()