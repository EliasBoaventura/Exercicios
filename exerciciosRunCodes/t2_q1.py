import math

valor_raio = float(input())
circunferencia = (2*3.141592) * (valor_raio)
area_circulo = 3.141592 * (math.pow(valor_raio, 2))
area_esfera = 4 * area_circulo
volume = 4/3 * 3.141592 * (math.pow(valor_raio, 3))

print('{:.6f}\n{:.6f}\n{:.6f}\n{:.6f}'.format(circunferencia, area_circulo, area_esfera, volume))