# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# 1 metros = 100 centímetros
# 1 metros = 1000 milímetros

# -> Se digitar o valor de metros 5, o print mostrara o resultado de ->

m = float(input('Digite um valor em metros: '))  # -> Digite um valor em metros: 5
cm = m * 100  # -> cm = 5 * 100
mm = m * 1000  # -> mm = 5 * 1000
print(f'{m} metros = {cm} centímetros')  # -> 5.0 metros 500.0 centímetros
print(f'{m} metros = {mm} milímetros')  # -> 5.0 metros 5000.0 milímetros
