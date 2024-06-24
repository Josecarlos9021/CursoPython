print('====== 10 termos de uma P.A ======')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
contador = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while contador <= total:
        print('{}'.format(termo), end=' -> ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar ainda? '))
print('Progressão finalizada. O total de termos foram {}.'.format(total))
