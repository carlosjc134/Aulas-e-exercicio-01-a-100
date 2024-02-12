# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras tem sem considerar espaços
# - Quantas letras tem o primeiro nome.

nome = input("Digite seu nome completo: ").strip()

print("Analisando seu nome...")
print("Seu nome em maíusculo é: ", nome.upper())
print("Seu nome em minúscula é: ", nome.lower())

separa = nome.split()

print(f"Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras")
