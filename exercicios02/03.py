ano_nascimento = int(input('Em que ano você nasceu? '))
ano_requerido = int(input('Para qual ano você quer saber sua idade? '))

calculo_idade = ano_requerido - ano_nascimento

print('No ano {} você terá {} anos!'.format(ano_requerido, calculo_idade))