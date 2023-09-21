numero_um = 3
numero_dois = 4
numero_tres = 8



menor = min(numero_um, numero_dois, numero_tres)
maior = max(numero_um, numero_dois, numero_tres)

exemplo_lista = [numero_um, numero_dois, numero_tres]
if(menor in exemplo_lista):
    exemplo_lista.remove(menor)
if(maior in exemplo_lista):
    exemplo_lista.remove(maior)
intermediario = exemplo_lista[0]
intermediario = int(intermediario)  
print((exemplo_lista[0]))    