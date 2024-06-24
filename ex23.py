num = str(input('Digite um número de 0 a 9999: ')).zfill(4)
print('O número digitado foi: {}'.format(num))
print('A sua unidade é: {}'.format(num[3]))
print('A sua dezena é: {}'.format(num[2]))
print('A sua centena é: {}'.format(num[1]))
print('A sua milha é: {}'.format(num[0]))

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

