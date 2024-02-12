# Crie um programa que leia o nome e o preço de varias produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = 0
totalmil = 0
menor = 0
cont = 0
barato = ""

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totalmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '

    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print("FIM DO PROGRAMA")
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')