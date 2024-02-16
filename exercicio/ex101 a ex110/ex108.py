# Adapte o codigo do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

def aumentar(preço=0, taxa=0):
    res = preço + (preço * taxa / 100)
    return res


def diminuir(preço=0, taxa=0):
    res = preço - (preço * taxa / 100)
    return res


def dobro(preço=0):
    res = preço * 2
    return res


def metade(preço=0):
    res = preço / 2
    return re


def moeda(preço=0, moeda='R$'):
    return f"{moeda}{preço}".replace('.', ',')


from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')