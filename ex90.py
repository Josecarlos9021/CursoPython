'''aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]:.1f}')
if aluno["media"] >= 7:
    print(f'Situação é igual a aprovado')
else:
    print('Situação é igual a reprovado')'''

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação]'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')