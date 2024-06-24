def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é {a:.1f}m².')
print('Controle de terrenos')
print('-' * 20)


largura = float((input('Largura (m): ')))
comprimento = float(input('Comprimento (m): '))

area(largura, comprimento)