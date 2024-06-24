altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print('A dimensão da sua parede é {} x {}, então a área é {}mª. logo, a quantidade necessárias de tinta são {} litros'.format(altura, largura,area, (area/2)))