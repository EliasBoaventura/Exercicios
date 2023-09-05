#escreva um programa que ler o valor para um lado de um quadrado. Calcule o mostre a área e o perímetro desse quadrado.

lado_do_quadrado = input().strip()
lado_do_quadrado = float(lado_do_quadrado)





def area(lado):
    return (lado * lado)

def perimetro(lado):
    return (lado * 4)

print(f'{area(lado_do_quadrado):>10.4f}')
print(f'{perimetro(lado_do_quadrado):>10.4f}')

