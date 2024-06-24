print('====== Tabuada ======')
'''contador = 0
num = int(input('Quer ver a tabuada de que valor? '))
while contador <10:
    contador += 1
    resultado = num * contador
    if num < 0:
        break
    else:
        print(f'{num} x {contador} = {resultado}')
    if contador >=10:
        num = int(input('Gostaria de ver a tabuada de qual valor? '))
        contador = 0
print('='*40)
print('Programa encerrado. Volte sempre!')
print('='*40)'''

while True:
    num = int(input('Quer ver a tabuada de que valor? '))
    print('-'*40)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-'*40)
print('Programa encerrado. Volte sempre!')



