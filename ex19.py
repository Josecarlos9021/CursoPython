from random import choice

pessoa1 = str(input('Nome do primeiro aluno: '))
pessoa2 = str(input('Segundo aluno: '))
pessoa3 = str(input('Terceiro aluno: '))
pessoa4 = str(input('Quarto aluno: '))
lista = [pessoa1, pessoa2, pessoa3, pessoa4]
aleatorio = choice(lista)
print('O aluno escolhido para apagar o quadro foi {}'.format(aleatorio))
