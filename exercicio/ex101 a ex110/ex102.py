# Crie um programa que tenha uma função fatorial()
# que receba dois parâmetros:
# um número que irá ser calculado o fatorial e outro chamado de show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela
# o processo de cálculo do fatorial.


def fatorial(n, show=False):

    """
    -> Calcule o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    : return: O valor do Fatorial de um número n.
    """

    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal

print(fatorial(5, show=True))
print(fatorial(5))
print("-=" * 25)
print(fatorial(10, show=True))
print(fatorial(10))
print("-=" * 25)
help(fatorial)
