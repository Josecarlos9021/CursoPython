valor = float(input('Digite seu salário: R$'))
salario = valor * 0.15
resultado = valor + salario
print('O salário de R${:.2f}, com reajuste de 15% do seu salário, o novo valor é R${:.2f}'.format(valor, resultado))