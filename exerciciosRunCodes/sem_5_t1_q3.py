#Escreva um programa que leia um preço e um valor percentual. Informe o preço com o aumento percentual e o preço com o desconto percentual. 
#Por exemplo, se for lido um preço de 100.00 e o valor percentual de 5 o programa deve mostrar que o preço com aumento é 105.00 e o preço com desconto é 95.00.

preco = input()
valor = input()

preco = float(preco)
valor = float(valor)

aumento = preco + (preco * valor/100)
desconto = preco - (preco * valor/100)

print(f'{aumento:.2f}\n{desconto:.2f}')
