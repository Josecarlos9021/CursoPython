jogador = dict()
partidas = list()
print('====== JOGADOR DE FUTEBOL ======')
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"].lower()} jogou? '))
for c in range(0, tot):
    partidas.append (int(input(f'Quantos gols na partida {c+1}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*40)
print(jogador)
print('-='*30)
for n, l in jogador.items():
    print(f'O campo {n} tem o valor {l}.')
print('-='*30)
print(f'O jogador {jogador["nome"].lower()} jogou {len(partidas)} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')



