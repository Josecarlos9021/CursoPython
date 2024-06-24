# forma clássica de fazer
#print('====== Calcule se o ano é bissexto ======')
#ano = int(input('Digite o ano que você nasceu: '))
#if ano % 4 == 0:
    # print('O ano que você nasceu é bissexto!')
#else:
    # print('O ano que você nasceu não é bissexto.')
from datetime import date
print('====== Calcule se o ano é bissexto ======')
ano = int(input('Digite o ano para analisar. Se digitar 0 sabéra o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
