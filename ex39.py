from datetime import date
print('====== Alistamento ======')
nascimento = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar agora mesmo!!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento!'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será no ano de {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos!'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi no ano de {}'.format(ano))
