# Escreva um programa que leia dois valores e mostre na tela, nessa ordem: 
# a. A soma dos números; 
# b. A concatenação das strings; 
# c. A multiplicação dos números; 
# d. A multiplicação como strings; 
# e. A divisão dos números; 
# f. A exponenciação; 
# g. O módulo (resto).

valor_um = input()
valor_dois = input()

valor_um = float(valor_um)
valor_dois = int(valor_dois)

soma = valor_um + valor_dois
concatenacao = str(valor_um) + str(valor_dois)
multiplicacao = valor_um * valor_dois
multiplicacao_strings = str(valor_um) * valor_dois
divisao = valor_um / valor_dois
divisao_inteira = valor_um // valor_dois
exponenciacao = valor_um ** valor_dois
resto = valor_um % valor_dois

print(f'{soma}\n{concatenacao}\n{multiplicacao}\n{multiplicacao_strings}\n{divisao}\n{divisao_inteira}\n{exponenciacao}\n{resto} ')
