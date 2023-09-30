# 05. Escreva um programa que leia o número de matrícula de um aluno, suas notas em 3 provas e a média das notas
# obtidas nos exercícios que fazem parte da sua avaliação. Calcule a média final usando a fórmula:
#     Média Final = (Nota 1 + Nota 2 ∗ 2 + Nota 3 ∗ 3 + Média Exercícios)/7
# A atribuição dos conceitos obedece a tabela abaixo.

# Conceito Média Final
# A >= 9.0
# B >= 7.5 e < 9.0
# C >= 6.0 e < 7.5
# D >= 4.0 e < 6.0
# E < 4.0

# O programa deve escrever a matrícula do aluno, a média final, o conceito correspondente e a mensagem “Aprovado”
# se o conceito for A, B ou C ou “Reprovado” se o conceito for D ou E.


def calcular_media(nota_um, nota_dois, nota_tres, media_exercicios):
    media_final = (nota_um + (nota_dois * 2) + (nota_tres * 3) + media_exercicios)/7
    
    return media_final

def mostrar_conceito(nota_um, nota_dois, nota_tres, media_exercicios):
    media_final = calcular_media(nota_um, nota_dois, nota_tres, media_exercicios)
    status = ''
    if(media_final >= 9.0):
        status = 'A'
    if(media_final >= 7.5 and media_final < 9.0):
        status = 'B'
    if(media_final >= 6.0 and media_final < 7.5):
        status = 'C'
    if(media_final >= 4.0 and media_final < 6.0):
        status = 'D'
    if(media_final < 4.0):
        status = 'E'
    return status

def aluno_aprovado(nota_um, nota_dois, nota_tres, media_exercicios):
    status_final = mostrar_conceito(nota_um, nota_dois, nota_tres, media_exercicios)
    status = ''

    if (status_final in ('A,B,C')):
        status = 'Aprovado'
    elif (status_final  in ('D,E')):
        status = 'Reprovado'
    else:
        raise ValueError('Entrada Invalida')

    return status

def main():
    matricula_aluno = input().strip()
    nota_um = float(input())
    nota_dois = float(input())
    nota_tres = float(input())
    media_exercicios = float(input())

    resultado_media = calcular_media(nota_um, nota_dois, nota_tres, media_exercicios)
    resultado_conceito = mostrar_conceito(nota_um, nota_dois, nota_tres, media_exercicios)
    resultado_aprovacao = aluno_aprovado(nota_um, nota_dois, nota_tres, media_exercicios)

    print(f'{matricula_aluno}\n{resultado_media:.2f}\n{resultado_conceito}\n{resultado_aprovacao}')



if __name__ == '__main__':
    main()