#Faça um programa que tenha uma função lista chamada números, e duas funções chamadas sorteio() e somaPar(). A primeira função vai so sortear 5 números e colocar-los dentro de uma lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
def sorteio(lista):
  from random import randint
  for cont in range(0, 5):
    n = randint(1, 10)
    lista.append(n)
  print('Sorteando 5 valores da lista: ', end='')
  for i, v in enumerate(lista):
    print(f'{v} ', end='', flush=True)
    sleep(0.5)
  print('PRONTO!')
def somaPar(lista):
  soma = 0
  for valor in lista:
    if valor % 2 == 0:
      soma += valor
  print(f'Somando os valores pares de {lista}, temos {soma}.')
# Programa principal
num = list()
sorteio(num)
somaPar(num)