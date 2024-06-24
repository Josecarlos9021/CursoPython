from time import sleep
print('\033[35m====== Contagem regressiva ======\033[m')
print('Lançamento dos fogos será em: ')
for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)
print('\033[1;33mFogos estourando!!!!\033[m')
sleep(1)
print('\033[1;31mBOMMMMMMMMMMMMMMMMMMMMMMMMMM!!!!')
sleep(2)
print('BOMMMMMMMMMMMMMMMMMMMMMMMMMM!!!!\033[m')
sleep(2)
print('\033[1;36mFeliz ano novo!!!!!!!!!!!!!\033[m')