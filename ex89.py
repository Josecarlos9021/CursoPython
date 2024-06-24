ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    res = str(input('Quer continuar? [S/N] '))
    if res in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:7.1f}')
while True:
    print('-='*35)
    opcao = (int(input('Mostrar notas de qual aluno? (999 interrompe): ')))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    if opcao <= len(ficha) -1:
        print(f'As notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('<<< VOLTE SEMPRE >>>')


