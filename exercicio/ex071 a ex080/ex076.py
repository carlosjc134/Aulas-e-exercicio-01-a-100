# Crie um programa que tenha uma tupla unica
# com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 1.75, 'Borracha' , 2,
            'Caderno', 15.90, 'Estojo', 25,
            'Travessão', 9.99, 'Mochila', 120.3,
            'Canetas', 22.3, 'Livro', 34.90)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-'*40)