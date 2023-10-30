def calcula_juros_sobre_capital(capital, juros_do_capital, valor_do_bem, juros_do_bem):
    quantidade_mes = 0
    while(valor_do_bem > capital):
        capital += capital * juros_do_capital/100
        valor_do_bem += valor_do_bem * juros_do_bem/100
        quantidade_mes += 1
    return quantidade_mes    
    

def main():
    valor_do_bem = input().strip()
    valor_do_bem = int(valor_do_bem)
    juros_bem = 0.4
    capital = 10000
    juros_capital = 0.7
    
    resultado = calcula_juros_sobre_capital(capital, juros_capital, valor_do_bem, juros_bem)

    print(resultado)

if __name__ == '__main__':
    main()