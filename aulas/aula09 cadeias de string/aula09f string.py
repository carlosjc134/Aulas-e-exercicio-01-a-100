palavra = "banana"
print(type(palavra))  # <class 'str'>
print(palavra.find("b"))  # ->find<- procurar letra posição  0
print(palavra.find("n"))  # ->find<- procurar letra posição  2
print(palavra.find("z"))  # ->find<- procurar letra posição -1

for letra in palavra:
    print(letra)
