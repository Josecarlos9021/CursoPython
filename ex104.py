def leiaint(mensagem):
    ok = False
    valor = 0
    while True:
        num = str(input(mensagem))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[1;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

num = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {num}.')