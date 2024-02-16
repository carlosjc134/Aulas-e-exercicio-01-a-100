#Crie um programa que tenha uma função fatorial() que receba dois parâmteros: um número que irá ser calculado o fatorial e outro chamad de show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n, show=False):
  f = 1
  for c in range(n, 0, -1):
    if show:
      print(c, end='')
      if c > 1:
        print(' x ', end='')
      else:
        print(' = ', end='')
    f *= c
  return f
# Programa principal
print(fatorial(5, show=True))
print(fatorial(10))
print(fatorial(10, show=True))