#print('====== Cálculo de multa ======')
#velmax = float(input('Qual a sua velocidade em km/h: '))
#vel = (velmax - 80) * 7
#print('Você foi multado! O valor da multa é R${}'.format(vel))

#print('====== O valor da multa é R$7.00 por km! ======')

print('====== Cálculo de multa ======')

vel = float(input('Qual a sua velocidade em km/h: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi multado! O limite é 80 km/h. A sua multa é R${}'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')
print('====== O valor da multa é R$7 por km ultrapassado!')
