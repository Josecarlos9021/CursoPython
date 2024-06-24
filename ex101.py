def voto(anonasc):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - anonasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return "Voto negado"
    elif 16 <= idade < 18 or idade >= 65:
        return "Voto opcional"
    else:
        return "Voto obrigatório"
print('-'*30)
anonasc = int(input('Em que ano você nasceu? '))
print(f'{voto(anonasc)}.')








