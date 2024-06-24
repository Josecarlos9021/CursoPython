from random import shuffle

pessoa1 = str(input('Nome do primeiro aluno: '))
pessoa2 = str(input('Segundo aluno: '))
pessoa3 = str(input('Terceiro aluno: '))
pessoa4 = str(input('Quarto aluno: '))
lista = [pessoa1, pessoa2, pessoa3, pessoa4]
shuffle(lista)
print('A ordem do grupo para começar a apresentação será:')
print(lista)