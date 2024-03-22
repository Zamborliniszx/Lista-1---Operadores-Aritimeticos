import math

raio = int(input('Digite o raio da esfera: '))

area = 4 * math.pi * raio ** 2
area = round(area, 2)

print('A área da esfera é:', area)