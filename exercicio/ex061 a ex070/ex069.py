# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

total18 = 0
totalHomens = 0
totalMulher20 = 0

while True:
    idade = int(input('idade: '))
    sexo = " "

    while sexo not in 'MF':
        sexo = str(input('sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == "M":
        totalHomens += 1
    if sexo == "F" and idade < 20:
        totalMulher20 += 1

    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {total18}")
print(f"Ao todo temos {totalHomens} homens cadastrados")
print(f"E temos {totalMulher20} mulheres com menos de 20 anos")
