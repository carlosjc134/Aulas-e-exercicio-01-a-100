valores = list(range(4,11))
print(valores)  # -> mostrara [4, 5, 6, 7, 8, 9, 10]

valores = list(range(4,11,2))
print(valores)  # -> mostrara [4, 6, 8, 10]

valores = [8,2,5,4,9,3,0]
print(valores)  # -> mostrara [8, 2, 5, 4, 9, 3, 0]

valores.insert(2, 3)  # inserir o 3 na posição 2
# ------------------> antes [8, 2, 5, 4, 9, 3, 0]
print(valores)  # -> depois [8, 2, 3, 5, 4, 9, 3, 0]

valores.sort()  # organiza os números em ordem crescente
print(valores)  # -> mostrara [0, 2, 3, 3, 4, 5, 8, 9]

valores.sort(reverse=True)  # organiza os números em ordem descrescente
print(valores)  # -> mostrara [9, 8, 5, 4, 3, 3, 2, 0]

print(len(valores))  # quantos elementos tem na lista -> mostrara 8


