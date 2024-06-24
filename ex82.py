numero = list()
while True:
    numero.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso...')

    res = str(input('Quer continuar? [S/N] '))
    if res in 'Nn':
        break

par = []
impar = []
for valor in numero:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
numero.sort()
par.sort()
impar.sort()
print(f'Os números digitados na lista são {numero}')
print(f'Os números pares da lista são {par}')
print(f'Os números ímpares da lista são {impar}')
