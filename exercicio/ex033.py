# Faça um programa que leia tres números e mostre qual é o maior e qual é o menor.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

menor = a

if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

maior = a

if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")
