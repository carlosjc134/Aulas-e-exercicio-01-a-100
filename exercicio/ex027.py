# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Digite seu nome completo: ").strip()
separa = nome.split()
print("Seu primeiro nome é: ", separa[0])
print("Seu último nome é: ", separa[len(separa)-1])
