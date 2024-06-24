print('====== Sequência de Fibonacci ======')
n = int(input('Quantos números você quer mostrar? '))
t1 = 0
t2 = 1
print('_'*30)
print('{} > {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' > {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' > FIM')
print('_'*30)
