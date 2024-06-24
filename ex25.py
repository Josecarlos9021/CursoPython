nome = str(input('Digite seu nome: ')).strip()
nome = nome.upper()
nome = 'SILVA' in nome
print('Seu nome possui Silva? {}'.format(nome))

nome = str(input('Digite seu nome: ')).strip()
print('Seu nome possui Silva? {}'.format('SILVA' in nome.upper()))
