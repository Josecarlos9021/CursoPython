num = list()
for c in range(1, 8):
    num.append(int(input(f'Digite o {c}º valor: ')))
    par = num[:]
    impar = num[:]
    par.clear()
    impar.clear()
for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
par.sort()
impar.sort()
print('='*30)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímpares digitados foram: {impar}')
