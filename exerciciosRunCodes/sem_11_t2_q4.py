def cardapio():
    print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
    
def tabela_valores(codigo_produto):
    valor = 0
    codigo_produto = str(codigo_produto).upper()
    if(codigo_produto == 'H'):
        valor += 5.50
    elif(codigo_produto == 'C'):
        valor += 6.80
    elif(codigo_produto == 'M'):
        valor += 4.50   
    elif(codigo_produto == 'A'):
        valor += 7.00
    elif(codigo_produto == 'Q'):
        valor += 4.00 
    return valor
    
def main():
    total_conta = 0.0
    while True:
        cardapio()
        codigo_digitado = input().strip()   
        if(codigo_digitado == 'X' or codigo_digitado == 'x'):
            break
        total_conta += tabela_valores(codigo_digitado)
    print(f'{total_conta:.2f}')
if __name__=='__main__':
    main()