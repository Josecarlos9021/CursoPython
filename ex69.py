tot18 = mulher20 = tothomem = 0
while True:
    print('====== Cadastre uma pessoa ======')
    print('='*33)
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: '))[0].upper().strip()

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] '))[0].upper().strip()
    if resp == 'N':
        break
print('\033[1;32m=' * 10, 'Fim do programa!', '=' * 10, '\033[m')
if tot18 == 1:
    print(f'\033[1;31mA quantidade de pessoas maiores que 18 anos foram apenas {tot18}\033[m')
else:
    print(f'\033[1;31mA quantidade de pessoas maiores que 18 anos foram {tot18}\033[m')
if tothomem == 1:
    print(f'\033[1;34mForam cadastrados {tothomem} homem.\033[m')
else:
    print(f'\033[1;34mForam cadastrados {tothomem} homens.\033[m')
if mulher20 == 1:
    print(f'\033[1;33mA quantidade de mulheres menores que 20 anos foram apenas {mulher20}\033[m')
else:
    print(f'\033[1;33mA quantidade de mulheres menores que 20 anos foram {mulher20}\033[m')



