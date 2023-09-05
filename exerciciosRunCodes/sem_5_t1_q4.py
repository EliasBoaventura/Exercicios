#Escreva um programa que leia uma determinada quantidade de minutos e informe essa quantidade convertidade para horas e minutos.
#Por exemplo, 220 minutos é equivalente 3 horas e 40 minutos.

minutos = input()
minutos = int(minutos)

horas = minutos // 60
minutos_restantes = minutos - (horas * 60)

print(f'{horas}:{minutos_restantes}')