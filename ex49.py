print('======= TABUADA =======')
num = int(input('Digite o número para saber a tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))