def fatorial(n=1, show=False):
    """
            -> Calcula o fatorial de um número.
            :param n: o número a ser calculado.
            :param show (opcional) mostrar ou não a conta.
            :return: o valor do fatorial de um número n.
        """

    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(f' x', end=' ')
            else:
                print(' = ', end='')
    return f


print('-'*25)
print(fatorial(5, show=True))