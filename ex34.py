print('====== Reajuste de salário ======')
salario = float(input('Digite o valor do seu salário? R$'))
if salario > 1250:
    novosalario = salario * 0.10 + salario
    print('O seu salário de R${:.2f} com o reajuste vai ficar R${:.2f}'.format(salario, novosalario))
else:
    novosalario = salario * 0.15 + salario
    print('O seu salário de R${:.2f} com o reajuste vai ficar R${:.2f}'.format(salario, novosalario))