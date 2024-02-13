# Desenvolva um programa que leia
# o primeiro termo e a razão de uma PA.
# No fim, mostre os 10 primeiros termos dessa progressão.

print('Gerador de PA')
print('-='*10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
cont = 1

while cont <= 10:
  print('{} -> '.format(termo), end='')
  termo += razao
  cont += 1
print('FIM')
