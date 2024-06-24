'''valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        print('Valor adicionado com sucesso...')
        resp = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
    if resp == 'N':
        break
print()
valores.sort()
print(f'O resultado foi {valores}')'''


numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Número duplicado! Não vou adicionar.')

    res = str(input('Quer continuar? [S/N] '))[0]
    if res in 'Nn':
        break
print('=-='*30)
print()
numeros.sort()
print(f'O resultado dos valores adicionado foi {numeros}')