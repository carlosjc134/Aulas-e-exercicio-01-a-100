# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pessoa in range(1, 8):
    nascimento = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print()

print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))
