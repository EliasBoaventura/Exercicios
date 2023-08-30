# Escreva um programa que leia uma quantidade de minutos e mostre a quantidade de horas e minutos equivalente.

quantidade_minutos = int(input())
quantidade_horas = quantidade_minutos // 60
quantidade_minutos_restantes = (quantidade_minutos - (quantidade_horas * 60))

print(f'{quantidade_horas}h{quantidade_minutos_restantes}min')