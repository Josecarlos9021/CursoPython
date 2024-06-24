print('====== Comparações de números ======')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O primeiro valor {} é maior!'.format(num1))
elif num2 > num1:
    print('O segundo valor {} é maior!'.format(num2))
else:
    print('O valor {} e {} são iguais!'.format(num1, num2))
print('====== FIM DO PROGRAMA ======')