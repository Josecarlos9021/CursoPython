print('====== Digite 3 valores para saber o maior deles e o menor! ======')
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número foi {}'.format(menor))
print('O maior número foi {}'.format(maior))
