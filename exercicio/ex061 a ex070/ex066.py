# Crie um programa que leia varios números inteiros pelo teclado.
# O programa só vai parar
# quando o usuário dizer que quer parar quando o usuário digitar o valor 999,
# que é a condição de parada.
# No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
cont = 0

while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} valores foi {soma}!')