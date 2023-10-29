
def nota_equivalente(nota):
    if(nota >= 8.5):
        print('A')
    elif(nota >= 7.0):
        print('B')
    elif(nota >= 5.0):
        print('C')    
    elif(nota >= 4.0):
        print('D')
    elif(nota >= 0.0):
        print('E')

def main():
    while True:
        nota_aluno = float(input())
        if nota_aluno > 10 or nota_aluno < 0:
            print('Nota inválida.')
            continue
        nota_equivalente(nota_aluno)
    


if __name__=='__main__':
    main()