numero = list()
cont = 0
while True:
    numero.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso...')
    cont += 1
    res = str(input('Quer continuar? [S/N] '))
    if res in 'Nn':
        break
print()
print(f'Foram adicionados {cont} números.')
numero.sort(reverse=True)
print(f'A ordem de forma decrescente é {numero}')
if 5 in numero:
    print('O número 5 foi adicionado a lista.')
else:
    print('O número 5 não foi adicionado a lista.')



