#Faça um programa que tenha uma função notas() que pode receber vária notas de alunos e vai retornar um dicionário com as seguintes informações:
#a) Quantidade de notas
#b) A maior nota
#c) A menor nota
#d) A média da turma
#e) A situação (opcional)
#Adicione também as docstrings dessa função para que help() funcione.
def notas(*n, sit=False):
  """
  -> Função para analisar notas e situações de vários alunos.
  :param n: uma ou mais notas dos alunos (aceita várias)
  :param sit: valor opcional, indicando se deve ou não adicionar a situação
  :return: dicionário com várias informações sobre a turma
  """
  r = dict()
  r['total'] = len(n)
  r['maior'] = max(n)
  r['menor'] = min(n)
  r['média'] = sum(n) / len(n)
  if sit:
    if r['média'] >= 7:
      r['situação'] = 'BOA'
    elif r['média'] >= 5:
      r['situação'] = 'RAZOÁVEL'
    else:
      r['situação'] = 'RUIM'
  return r
# Programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
