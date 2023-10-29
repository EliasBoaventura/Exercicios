
def main():
    valor_salario = input()
    valor_divida = input()
    valor_salario = float(valor_salario)
    valor_divida = float(valor_divida)
 
    mes = 10
    ano = 2016


    while(valor_salario>valor_divida):
        if(mes == 3):
            valor_salario += valor_salario * 0.05
            
        valor_divida += valor_divida * 0.15    
        if(mes == 12):
            mes = 0
            ano += 1
        mes += 1

    print(mes, "/", ano,sep='')
if __name__=='__main__':
    main()