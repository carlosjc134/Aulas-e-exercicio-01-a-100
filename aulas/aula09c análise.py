frase = 'Curso em Vídeo Python'

print(len(frase))  # Quantas letras tem na frase.
print(frase.count("o"))  # Quantas vezes aparece a letra "o" na frase
print(frase.count("o", 0, 13))  # Quantas vezes aparece a letra "o" na frase entre o '0 até o 13'.
print(frase.find("deo"))  # Em qual posição começou a frase "deo"
print(frase.find("Android"))  # Quando uma palavra não é encontrada retorna -1.
print("curso" in frase)  # analisa se tem a a palavra na frase. retorna True ou False.

