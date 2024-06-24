from datetime import date
print('====== Idade ======')
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nasc = int(input(('Digite a {}º ano de nascimento: '.format(pessoa))))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Tivemos {} maiores de idade'.format(totalmaior))
print('E tivemos {} menores de idade'.format(totalmenor))