pessoas = dict()
galera = list()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas o M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        res = (input('Quer continuar? [S/N]: ')).upper()[0]
        if res in 'SN':
            break
        print('ERRO! Por favor, digite apenas o S ou N.')
    if res == 'N':
        break
media = soma / len(galera)
print('-='*30)
print(f'A)    O grupo tem {len(galera)} pessoas.')
print(f'B)    A média de idade é de {media:5.2f}' )
print('C)    As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'[{p["nome"]}] ', end='')
print()
print('D)    Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('      ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print('<< ENCERRADO >>')