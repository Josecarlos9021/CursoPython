from random import randint
from time import sleep
num = [randint(1, 10) for c in range(5)]
pares = list()
def sorteio(num):
    print(f'Sorteando 5 valores da lista: {num}, PRONTO!', flush=True)
    sleep(0.4)


for par in num:
    if par % 2 == 0:
        pares.append(par)


def somarPar(pares):
    soma = sum(pares)
    print(f'Somando os valores pares de {num}, temos {soma}!')


sorteio(num)
somarPar(pares)





