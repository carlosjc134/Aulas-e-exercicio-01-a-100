# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Precisamos receber o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal,
# sabe-se que ela não pode exceder 30% do salário ou então o empréstimo mo será negado.

print('='*30)
print('{:^30}'.format('BANCO XYZ'))
print('='*30)
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end='')
print(f' a prestação será de R${prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
