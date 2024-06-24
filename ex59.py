num1 = int((input('Digite o primeiro número: ')))
num2 = int((input('Digite o segundo número: ')))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print('O resultado da soma de {} + {} é {}'.format(num1, num2, soma))
    elif opcao == 2:
        mult = num1 * num2
        print('O resultado da multiplicação de {} x {} é {}'.format(num1, num2, mult))
    elif opcao == 3:
        maior = num1
        if num2 > num1:
            maior = num2
        print('O maior número entre {} e {} é o {}'.format(num1, num2, maior))
    elif opcao == 4:
        print('Informe novamente:')
        num1 = int((input('Digite o primeiro número: ')))
        num2 = int((input('Digite o segundo número: ')))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
print('Fim do programa. Volte sempre!')

