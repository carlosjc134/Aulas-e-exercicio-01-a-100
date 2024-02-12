# Refaça o desafio 009,
# mostrando a tabuada de um número que o usuário escolhe,
# só que agora utilizando um laço for.

n = int(input('Digite um número: '))

for c in range(1, 11):
    print(f'{n} x {c} = {n*c}')
