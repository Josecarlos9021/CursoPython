soma = num = quant = 0
while True:
    num = int(input('Digite um número (999 ele vai parar): '))
    if num == 999:
        break
    quant += 1
    soma += num
print(f'A soma dos {quant} valores foram {soma}.')