# crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# ex: digite um número: 6.127
# o número 6.127 tem a parte inteira 6.

import math

num = float(input('Digite um valor: '))
trunc = math.trunc(num)
int = int(num)

# # Com a função trunc
print(f'O valor digitado foi {num} e a sua porção inteira é {trunc}')

# Com a função int
print(f'O valor digitado foi {num} e a sua porção inteira é {int}')