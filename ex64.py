soma = 0
tudo = 0
num = 0
cont = 1
while num != 999:
    num = int(input('Digite um número inteiro [999 vai parar]: '))
    if num != 999:
        soma += cont
        tudo += num
print('A quantidade de números digitados foram {} e a soma entre eles foram {}.'.format(soma, tudo))
