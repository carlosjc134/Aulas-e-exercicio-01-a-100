# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
# o programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)

print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")

jogador = int(input('Em que número eu pensei: '))  # jogador tenta adivinhar

sleep(3)
if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')
