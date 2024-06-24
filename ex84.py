pessoa = list()
galera = list()
totalPessoa = maior = menor = 0
while True:
    galera.append(str(input('Digite seu nome: ')))
    galera.append(float(input('Digite seu peso(KG): ')))
    if len(pessoa) == 0:
        maior = menor = galera[1]
    else:
        if galera[1] > maior:
            maior = galera[1]
        if galera[1] < menor:
            menor = galera[1]
    pessoa.append(galera[:])
    galera.clear()
    totalPessoa += 1
    res = str(input('Quer continuar?[S/N]: '))
    if res in 'Nn':
        break

print('='*30)
print(f'O total de pessoas cadastradas foram {totalPessoa}.')
print(f'O maior peso foi de {maior}KG. Peso de ', end='')
for p in pessoa:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}KG. Peso de ',end='')
for p in pessoa:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()