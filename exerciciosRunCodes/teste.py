valor_total = 0.0
while True:
    print('CÓDIGO  PRODUTO         PREÇO (R$)')
    print('H       Hamburger       5,50')
    print('C       Cheeseburger    6,80')
    print('M       Misto Quente    4,50')
    print('A       Americano       7,00')
    print('Q       Queijo Prato    4,00')
    print('X       PARA TOTAL DA CONTA')

    codigo = input().upper().strip()
    if codigo == 'X':
        break  
    if codigo == 'H':
        valor_total += 5.50
    if codigo == 'C':
        valor_total += 6.80
    if codigo == 'M':
        valor_total += 4.50
    if codigo == 'A':
        valor_total += 7.00
    if codigo == 'Q':
        valor_total += 4.00

print(f'{valor_total:.2f}')