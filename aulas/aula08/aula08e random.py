import random

# random.randint()
# random.random()
# random.choice()  # -> escolhe um elemento aleatorio da sequência
# random.shuffle()   # -> embaralha a sequência

numero1 = random.randint(1, 50)  # -> gera um numero aleatorio entre os valores passados dentro dos parênteses.
print(numero1)

numero2 = random.random()  # -> gera um numero aleatorio entre 0 e 1
print(numero2)

numero3 = random.random() * 100  # -> gera um numero aleatorio float
print(numero3)

numero4 = random.random() * 100  # -> gera um numero aleatorio float
numero = int(numero4)  # -> transforma um numero float para int
print(numero)