# Crie um programa que pergunte "Quanto dinheiro você tem na carteira?"
# e mostre quantos dólares ela pode comprar.

real = float(input("Quanto dinheiro você tem na carteira?"))
dolar = real / 3.27

print(f"Com R${real:.2f} você pode comprar US${dolar:.2f}")
