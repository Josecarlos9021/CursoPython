print('====== Maior e menor peso ======')
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('{}º a digitar seu peso: KG'.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}KG'.format(maior))
print('O menor peso foi de {}KG'.format(menor))