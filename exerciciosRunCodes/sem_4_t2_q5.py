#Escreva um programa que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas são 2, 3 e 5. 
#Fórmula para o cálculo da média final é: média ponderada=((n12)+ (n23)+ (n3*5))/10

nota_um = input()
nota_dois = input()
nota_tres = input()

nota_um = float(nota_um)
nota_dois = float(nota_dois)
nota_tres = float(nota_tres)

media_ponderada = ((nota_um *2)+ (nota_dois* 3)+ (nota_tres*5))/10

print(media_ponderada)