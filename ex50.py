soma = 0
count = 0
for c in range(1, 7):
    num = int(input('Digite {} número: '.format(c)))
    if num % 2 == 0:
        soma += num
        count += 1
print('Você digitou {} pares, a soma desses números são {}.'.format(count, soma))
