# Escreva um programa que leia uma temperatura em graus Celsius e mostra na tela o valor correspondente em graus Fahrenheit: Fahrenheit = (Celsius x (9 / 5)) + 32
temperatura_celcius = input()

temperatura_celcius = float(temperatura_celcius)
temperatura_fahrenheit = (temperatura_celcius * (9 / 5)) + 32

print(temperatura_fahrenheit)