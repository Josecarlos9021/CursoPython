from random import randint
from time import sleep
from operator import itemgetter
jogador = dict()
racking = list()
print('Valores sorteados:')
for c in range(1, 5):
    num = randint(1, 6)
    jogador[f'Jogador {c}'] = num
    print(f'O jogador {c} tirou {num} no dado.')
    sleep(1)
racking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('  == Ranking dos jogadores ==')
for i, v in enumerate(racking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')

