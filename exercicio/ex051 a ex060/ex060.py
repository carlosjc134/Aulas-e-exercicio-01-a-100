# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
# Código do programa:

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1

print(f"Calculando {n}! = ", end="")
while c > 0:
    print(f"{c} ", end="")
    if c > 1:
        print("x ", end="")
    else:
        print("= ", end="")
    f *= c
    c -= 1
print(f"{f}")



