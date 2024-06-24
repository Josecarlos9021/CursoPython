def ficha(nome, gols):
    if not nome:
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: '))
print(ficha(nome, gols))
