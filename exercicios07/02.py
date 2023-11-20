alfabeto = "abcdefghijklmnopqrstuvwxyz"

chave = 12

letra = input('digite a letra: ')

posicao = alfabeto.find(letra)

nova_posicao = (posicao + chave) % 26

letra_criptografada = alfabeto[nova_posicao]
print('letra criptografada', letra_criptografada)

# reposta chave 7 letra d = 'k'
# reposta chave 4 letra x = 'b'
# reposta chave 12 letras omqemd = 'aycqyp'
