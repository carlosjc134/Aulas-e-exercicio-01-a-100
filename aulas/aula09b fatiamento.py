# fatiamento

frase = 'Curso em Vídeo Python'

mostrar = frase[9]  # -> mostrara a letra 9
print(mostrar)  # -> mostrara "V"

mostrar = frase[9:13]  # -> mostrara as letras do 9 ao 13
print(mostrar)  # -> mostrara "Víde"

mostrar = frase[9:21:2]  # mostrara as letras do 9 ao 21 pulando de 2 em 2
print(mostrar)  # -> mostrara "VdoPto"

mostrar = frase[9:21]  # mostrara as letras do 9 ao 21 pulando de 2 em 2
print(mostrar)  # -> mostrara "Python"

mostrar = frase[15:]  # mostrara as letras do 15 até o final da palavra
print(mostrar)  # -> mostrara "Python"

mostrar = frase[9::3]  # mostrara as letras do 9 até o final pulando de 3 em 3
print(mostrar)  # -> mostrara "VePh"
