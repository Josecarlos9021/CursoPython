#nome = str(input('Digite seu nome completo: ')).strip()
#dividido = nome.split()
#print('Seu primeiro nome é: {}'.format(dividido[0]))
#dividido1 = nome.rsplit()
#print('Seu último nome é: {}'.format(dividido1[0]))

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome) - 1]))
