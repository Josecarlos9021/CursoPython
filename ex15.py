dias = int(input('Quantidade de dias: '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('A quantidade de tempo rodados são {} dias e distância são {}km, então o preço a pagar é R${:.2f}'.format(dias, km, pago))