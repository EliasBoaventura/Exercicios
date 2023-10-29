def main():
    soma = []
    quantidade_numero_lidos  = 0
    while True:
        numero = int(input())
        if numero == 0:
            break
        soma.insert(quantidade_numero_lidos, numero)
        quantidade_numero_lidos+=1

    print(f'{max(soma)}',f'{min(soma)}',sep='\n')
if __name__=='__main__':
    main()