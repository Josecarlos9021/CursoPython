from datetime import date
print('====== Categoria de natação ======')
nascimento = int(input('Digite o ano do seu nascimento: '))
ano = date.today().year
ano = ano - nascimento

if ano <= 9:
    print('Você tem ou terá {} e a categoria adequada é a \033[33mMIRIM!\033[m'.format(ano))
elif ano <= 14:
    print('Você tem ou terá {} e a categoria adequada é a \033[32mINFANTIL!\033[m'.format(ano))
elif ano <= 19:
    print('Você tem ou terá {} e a categoria adequada é a \033[36mJUNIOR!\033[m'.format(ano))
elif ano <= 25:
    print('Você tem ou terá {} e a categoria adequada é a \033[34mSÊNIOR\033[m'.format(ano))
else:
    print('Você tem ou terá {} e a categoria adequada é a \033[35mMASTER\033[m'.format(ano))
print('====== Boa sorte nos treinamentos! ======')
