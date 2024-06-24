continuar = 'S'
media = 0
soma = 0
quant = 0
maior = 0
menor = 0
while continuar == 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Deseja continuar? ')).upper().strip() [0]
media = soma / quant
print('A quantidade dos números foram {} e a média dos número é {:.2f}'.format(quant, media))
print('O maior número foi {} e o menor {}'.format(maior, menor))