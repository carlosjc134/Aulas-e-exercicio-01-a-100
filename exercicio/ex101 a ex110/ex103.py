# Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais:
# o nome de um jogador e quanto gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa principal
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == "":
    ficha(gol=gols)
else:
    ficha(nome, gols)
