# 04. Escreva um programa que leia a data de nascimento do usuário, e informa qual o seu signo. Considere exatamente:
# Áries (21/03 a 19/04); Touro (20/04 a 20/05); Gêmeos (21/05 a 21/06); Câncer (22/06 a 22/07); Leão (23/07 a
# 22/08); Virgem (23/08 a 22/09); Libra (23/09 a 22/10); Escorpião (23/10 a 21/11); Sagitário (22/11 a 21/12);
# Capricórnio (22/12 a 19/01); Aquário (20/01 a 18/02); Peixes (19/02 a 20/03);


def identifica_signos(dia, mes):
    #21/03 a 19/04
    signo = ''
    if((dia >= 21 and mes == 3 ) or (dia <= 19 and mes == 4)):
        signo = 'Áries'
    #20/04 a 20/05   
    elif((dia >= 20 and mes == 4 ) or (dia <= 20 and mes == 5)):
        signo = 'Touro'
    #21/05 a 21/06
    elif((dia >= 21 and mes == 5 ) or (dia <= 21 and mes == 6)):
        signo = 'Gêmeos'
    #22/06 a 22/07   
    elif((dia >= 22 and mes == 6 ) or (dia <= 22 and mes == 7)):
        signo = 'Câncer' 
    #23/07 a 22/08  
    elif((dia >= 23 and mes == 7 ) or (dia <= 22 and mes == 8)):
        signo = 'Leão'      
    #23/08 a 22/09    
    elif((dia >= 23 and mes == 8 ) or (dia <= 22 and mes == 9)):
        signo = 'Virgem'  
    #23/09 a 22/10    
    elif((dia >= 23 and mes == 9 ) or (dia <= 22 and mes == 10)):
        signo = 'Libra'  
    #23/10 a 21/11    
    elif((dia >= 23 and mes == 10 ) or (dia <= 21 and mes == 11)):
        signo = 'Escorpião'  
    #22/11 a 21/12   
    elif((dia >= 22 and mes == 11 ) or (dia <= 21 and mes == 12)):
        signo = 'Sagitário'   
    #22/12 a 19/01           
    elif((dia >= 22 and mes == 12 ) or (dia <= 19 and mes == 1)):
        signo = 'Capricórnio' 
    #20/01 a 18/02    
    elif((dia >= 20 and mes == 1) or (dia <= 18 and mes == 2)):
        signo = 'Aquário' 
    #19/02 a 20/03    
    elif((dia >= 19 and mes == 2) or (dia <= 20 and mes == 3)):
        signo = 'Peixes' 
    else:
        return 'entrada invalida'
    return signo


def main():
    dia = input()
    mes = input()
    dia = int(dia)
    mes = int(mes)

    print(identifica_signos(dia, mes))
    

if __name__ =='__main__':
    main()     