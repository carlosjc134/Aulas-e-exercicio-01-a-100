galera = list()
dado = list()
totoalmaior = 0
totoalmenor = 0

for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totoalmaior += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totoalmenor += 1

print(f"Temos {totoalmaior} maiores e {totoalmenor} menores de idade")