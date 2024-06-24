print('====== Vamos jogar par ou ímpar ======')
from random import randint
vitoria = 0
while True:
    print('=' * 38)
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.')
    print('\033[1;36mDEU PAR!\033[m' if total % 2 == 0 else '\033[1;36mDEU ÍMPAR!\033[m')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[1;4;32mVOCÊ VENCEU!\033[m')
            vitoria += 1
        else:
            print('\033[1;4;31mVOCÊ PERDEU!\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[1;4;32mVOCÊ VENCEU!\033[m')
            vitoria += 1
        else:
            print('\033[1;4;31mVOCÊ PERDEU!\033[m')
            break
    print('\033[1;33mVamos jogar novamente...\033[m')
if vitoria == 1:
    print(f'\033[1;35mGAMER OVER!\033[m Você venceu {vitoria} vez.')
else:
    print(f'\033[1;35mGAMER OVER!\033[m Você venceu {vitoria} vezes.')
