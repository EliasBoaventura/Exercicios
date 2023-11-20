alfabeto = "abcdefghijklmnopqrstuvwxyz"

chave = int(input('digite a chave: '))

letra = input('digite a letra: ')

posicao = alfabeto.find(letra)

nova_posicao = (posicao + chave) % 26

letra_criptografada = alfabeto[nova_posicao]
print('letra criptografada', letra_criptografada)