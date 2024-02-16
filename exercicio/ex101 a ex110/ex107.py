#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
def aumentar(preço=0, taxa=0):
  res = preço + (preço * taxa / 100)
  return res
def diminuir(preço=0, taxa=0):
  res = preço - (preço * taxa / 100)
  return res
def dobro(preço=0):
  res = preço * 2
  return res
def metade(preço=0):
  res = preço / 2
  return res

from ex107 import moeda
# Programa principal
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')