
def ler_quantidade_pessoas():
    soma_idades = 0
    numero_pessoas = 0
    idade_media = 0
    idades = []
    
    while(True):
        idade = int(input())
        if(idade == 0):
            break
        idades.insert(numero_pessoas, idade)
        numero_pessoas += 1
        soma_idades += idade
    if(numero_pessoas):
        idade_media = soma_idades/numero_pessoas   

    return numero_pessoas, idade_media, max(idades), min(idades)
def main():
    numero_pessoas, idade_media, maior_idade, menor_idade = ler_quantidade_pessoas()

    print(f'{numero_pessoas}', f'{idade_media:.2f}', menor_idade, maior_idade, sep='\n')


if __name__=='__main__':
    main()