num = (int(input('Digite um número: ')),
       int(input('Digite o 2º número: ')),
        int(input('Digite o 3º número: ')),
        int(input('Digite o 4º número: ')))
print(f'Os valores são {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O 3 aparece na {num.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')