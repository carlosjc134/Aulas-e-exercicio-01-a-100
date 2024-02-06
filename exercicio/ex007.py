# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# -> se digitar esses valores 8.5 e 7.5, o print mostrara o resultado de 7.75

n1 = float(input('Digite a primeira nota: '))  # -> Digite a primeira nota: 8.5
n2 = float(input('Digite a segunda nota: '))  # -> Digite a segunda nota: 7.5
media = (n1 + n2) / 2  # -> media = (8.5 + 7.5) / 2

print(f'A média das notas é {media:.1f}')  # -> A média das notas é 8.0
