from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['ano'] = int(input('Ano de nascimento: '))
pessoa['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
anoatual = date.today().year
idade = anoatual - pessoa['ano']
pessoa['ano'] = idade
if pessoa["carteira"] != 0:
    pessoa['contratação'] = int(input('Ano de constratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = idade + ((pessoa['contratação'] + 35) - date.today().year)
print('-='*40)
for n, p in pessoa.items():
    print(f'    - O {n} tem o valor {p}')
