total = p1000 = cont = menor = 0
barato = ''
while True:
    print('====== Cadastre um produto ======')
    print('='*33)
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço: '))
    cont += 1
    total += preco

    if preco > 1000:
        p1000 += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] '))[0].upper().strip()
    if resp == 'N':
        break
print('\033[1;32m=' * 10, 'Fim do programa!', '=' * 10, '\033[m')
print(f'\033[1;33mO total da compra foi R${total:.2f}\033[m')
if p1000 == 1:
    print(f'\033[1;36mTemos apenas {p1000} produto acima de R$1000.00\033[m')
else:
    print(f'\033[1;36mTemos {p1000} produtos acima de R$1000.00\033[m')
print(f'\033[1;37mO produto mais barato foi {barato} e custa R${menor:.2f}\033[m')