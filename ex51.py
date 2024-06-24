print('====== 10 termos de uma P.A ======')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('Acabou')