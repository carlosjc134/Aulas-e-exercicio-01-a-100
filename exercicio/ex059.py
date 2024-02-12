# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.
print('='*30)
print('EXERCÍCIO Nº 044')
print('='*30)
print(' ')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print(' ')
print('='*30)
print('MENU')
print('='*30)
print(' ')
print('[ 1 ] somar')
print('[ 2 ] multiplicar')
print('[ 3 ] maior')
print('[ 4 ] novos números')
print('[ 5 ] sair do programa')
print(' ')
opcao = int(input('Digite a opção desejada: '))
print(' ')
if opcao == 1:
  print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
elif opcao == 2:
  print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
elif opcao == 3:
  if n1 > n2:
    print('O maior valor entre {} e {} é {}'.format(n1, n2, n1))
  else:
    print('O maior valor entre {} e {} é {}'.format(n1, n2, n2))
elif opcao == 4:
  n1 = int(input('Digite o primeiro valor: '))
  n2 = int(input('Digite o segundo valor: '))
elif opcao == 5:
  print('Finalizando...')
else:
  print('Opção inválida. Tente novamente.')
print(' ')
print('='*30)
print('FIM DO PROGRAMA')
print('='*30)