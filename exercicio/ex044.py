# Elabore um programa que calcule o valor a ser pago por um produto
# considerando o seu preço o e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

print(f"{'LOJAS GUANABARA':=^40}")
valor = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS")
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
else:
    total = valor
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print(f'Sua compra de R${valor:.2f} vai custar R${total:.2f} no final.')
