print('====== Valor da cobrar do ônibus ======')
distancia = float(input('Qual a distância em km da sua viagem? '))
if distancia <= 200:
    valor = distancia * 0.50
    print('A distãncia de {}km terá o valor da passagem de R${}'.format(distancia, valor))
if distancia > 200:
    valor = distancia * 0.45
    print('A distãncia de {}km terá o valor da passagem de R${:.2f}'.format(distancia, valor))