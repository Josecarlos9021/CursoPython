from time import sleep
def maior(* valores):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for num in valores:
        print(f'{num}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = num
        else:
            if num > maior:
                maior = num
        cont += 1
    print(f'foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


