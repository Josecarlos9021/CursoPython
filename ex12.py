valor = float(input('Digite o preço do produto: R$'))
preco = valor * 0.05
resultado = valor - preco
print('O produto que custava R${:.2f}, promoção de 5%, o novo preço é R${:.2f}'.format(valor, resultado))