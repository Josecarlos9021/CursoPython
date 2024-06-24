print('====== Loja do Juinão ======')
preco = float(input('Qual o valor do seu produto? R$'))
condição = str(input('''Qual a condição do pagamento? 
[1] à vista no dinheiro/cheque
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de juros
Digite a opção: '''))

if condição == '1':
    desconto = preco * 0.90
    print('O valor de R${:.2f} à vista com desconto de 10% fica R${:.2f}.'.format(preco, desconto))
elif condição == '2':
    desconto = preco * 0.95
    print('O valor de R${:.2f} à vista no cartão com desconto de 5% fica R${:.2f}.'.format(preco, desconto))
elif condição == '3':
    parcelamento = preco / 2
    print('O valor de R${:.2f} parcelado em 2x sem juros irá ficar {:.2f}.'.format(preco, parcelamento))
elif condição == '4':
    parcelado = int(input('Digite a quantidade de parcelas: '))
    juros = preco * 1.20 / parcelado
    print('O valor de R${:.2f} parcelado em {}x com juros irá ficar R${:.2f}'.format(preco, parcelado, juros))
    print('O valor total ficou R${:.2f}.'.format(preco * 1.20))
else:
    print('Opção inválida de pagamento. Tente novamente!')
