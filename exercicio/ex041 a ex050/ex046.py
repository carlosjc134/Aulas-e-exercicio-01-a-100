# Faça um programa que mostre na tela uma contagem regressiva para o estourar do foguete.
# Ex:
# 10
# 9
# 8
# ...
# 3
# 2
# 1
# 0
# Liftoff!

from time import sleep

for i in range(10, -1, -1):

    print(i)
    sleep(1)

print("BUM! BUM! BUM! ")
