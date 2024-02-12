lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata Frita")

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")
print(30 * "-=")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
print(30 * "-=")

