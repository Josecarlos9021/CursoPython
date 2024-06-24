print('\033[1;32m====== Empréstimo Bancário ======\033[m')
casa = float(input('Qual o valor da casa que você deseja? \033[32mR$\033[m'))
salario = float(input('Qual o valor do seu salário? \033[32mR$\033[m'))
ano = int(input('Em quantos anos você deseja pagar? '))
prestação = casa / (ano * 12)
minimo = salario * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação ficará R$ {:.2f}.'.format(casa, ano, prestação))

if prestação <= minimo:
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado!')
