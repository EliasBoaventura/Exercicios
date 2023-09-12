# 05. Você sabia que os pinguins usam jaquetas devido ao frio na Antártida? Vamos ajudá-los a converter temperaturas!
# Escreva um programa que leia uma temperatura em Celsius e mostre o resultado em Fahrenheit. Lembre-se:

# °F = (°C * (9/5)) + 32

def convercao(temperatura_em_celcius):
    temperatura_em_fahrenheit = (temperatura_em_celcius * 9/5) + 32
    return temperatura_em_fahrenheit

def main():
    temperatura = input()
    temperatura = float(temperatura)

    print(convercao(temperatura))


if __name__ == '__main__':
    main()    