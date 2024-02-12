# Faça um programa que leia o comprimento
# do cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

# usando o modulo math
hi1 = math.hypot(co, ca)

# sem o modulo math
hi2 = (co ** 2 + ca ** 2) ** (1/2)

print(f'A hipotenusa vai medir {hi1:.2f}')
print(f'A hipotenusa vai medir {hi2:.2f}')