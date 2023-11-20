alfabeto = "abcdefghijklmnopqrstuvwxyz"
frase = []
chave = 12
while True:
    letra = input('digite a letra: ')
    if letra == '0':
        break

    posicao = alfabeto.find(letra)

    nova_posicao = (posicao + chave) % 26

    letra_criptografada = alfabeto[nova_posicao]

    frase.append(letra_criptografada)


print('a frasecriptografada é:', frase)