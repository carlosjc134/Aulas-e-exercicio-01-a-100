# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
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
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1*n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior valor entre {n1} e {n2} é {n1}')
        else:
            print(f'O maior valor entre {n1} e {n2} é {n2}')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    sleep(2)
print(' ')
print('='*30)
print('FIM DO PROGRAMA')
print('='*30)
