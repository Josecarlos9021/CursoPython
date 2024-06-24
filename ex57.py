'''sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo da pessoa, [F] para feminino e [M] para o masculino: ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Errado! Digite seu sexo novamente: ')).upper()
if sexo == 'M':
    print('A pessoa é do sexo masculino!')
else:
    print('A pessoa é do sexo feminino!')'''
sexo = str(input('\033[33mInforme seu sexo: [M/F] \033[m')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('\033[31mDados inválidos. Digite novamente: \033[m')).strip().upper()[0]
print('\033[35mO sexo {} foi registrado.\033[m'.format(sexo))