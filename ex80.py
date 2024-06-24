lista = list()
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Adicionado na posição {pos}.')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados na ordem da lista foi {lista}')