# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))  # se o número digitado for "81"

# O print mostrara ->:
print(f'O dobro de {n} é {n*2}')  # -> O dobro de 81 é 162
print(f'O triplo de {n} é {n*3}')  # -> O triplo de 81 é 243
print(f'A raiz quadrada de {n:.2f} é {(n**(1/2)):.2f}')  # -> # A raiz quadrada de 81 é 9.00
