def numero_por_extenso(numero):
    # Dicionários com palavras correspondentes às unidades, dezenas e centenas
    unidades = ["", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centenas = ["", "cem", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
    
    # Divide o número em partes inteiras e decimais
    partes = str(numero).split('.')
    parte_inteira = int(partes[0])
    parte_decimal = int(partes[1]) if len(partes) > 1 else 0

    # Converte a parte inteira para extenso
    extenso_inteira = ""
    if parte_inteira >= 100:
        extenso_inteira += centenas[parte_inteira // 100] + " "
        parte_inteira %= 100
    if parte_inteira >= 10 and parte_inteira <= 19:
        extenso_inteira += "e" if extenso_inteira else ""
        extenso_inteira += unidades[parte_inteira] + " "
    else:
        if parte_inteira >= 20:
            extenso_inteira += dezenas[parte_inteira // 10] + " "
            parte_inteira %= 10
        if parte_inteira > 0:
            extenso_inteira += "e" if extenso_inteira else ""
            extenso_inteira += unidades[parte_inteira] + " "

    # Converte a parte decimal para extenso
    extenso_decimal = ""
    if parte_decimal > 0:
        extenso_decimal += "vírgula"
        for digito in str(parte_decimal):
            extenso_decimal += " " + unidades[int(digito)]

    # Combina as partes inteira e decimal
    extenso_final = extenso_inteira + extenso_decimal

    return extenso_final

# Teste com o exemplo
numero = input()
extenso = numero_por_extenso(numero)
print(extenso)
