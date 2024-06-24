def leiaint(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mErro: por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return f


inteiro = leiaint('Digite um inteiro: ')
real = leiaFloat(('Digite um real: '))
print(f'O valor inteiro digitado foi {inteiro} e o real {real}!')