frase = str(input('Digite uma frase: ')).strip().upper()
print('Quantas vezes aparece a letra: {}'.format(frase.count('A')))
print('Mostra na primeira vez na posição: {}'.format(frase.find('A') + 1))
print('Mostra na última posição: {}'.format(frase.rfind('A') + 1))