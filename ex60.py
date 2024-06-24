print('====== Cálculo de fatorial ======')
'''fatorial = 1
num = int(input('Digite um número: '))
while num > 0:
    fatorial = num * fatorial
    num -= 1
print('O resultado foi {}'.format(fatorial))'''

num = int(input('Digite um número: '))
contador = num
fatorial = 1
print('Calculando {}! '.format(num))
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))