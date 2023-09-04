# Escreva um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostra na tela a idade dessa pessoa expressa apenas em dias. 
# Considerar sempre os anos com 365 dias e os messes com 30 dias.

idade_anos = input().strip()
idade_meses = input().strip()
idade_dias = input().strip()

idade_anos = int(idade_anos)
idade_meses = int(idade_meses)
idade_dias = int(idade_dias)

idade_em_dias = (idade_anos * 365) + (idade_meses * 30) + idade_dias

print(idade_em_dias)