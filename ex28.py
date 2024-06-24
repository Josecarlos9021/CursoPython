import random
import time
print('\033[1;33m====== Inicio do jogo! ======\033[m')
num = int(input(('Qual o número que o computador irá digitar de 0 a 5? ')))
aleatorio = random.randint(0, 5)
print('\033[34mO número escolhido pelo programa é {}.\033[m'.format(aleatorio))
print('\033[1;35mProcessando...\033[m')
time.sleep(2)
if num == aleatorio:
    print('\033[31mParabéns, você acertou o número escolhido pelo programa! Cãmbio, desligo...\033[m')
else:
    print('\033[32mEu ganhei! Eu escolhi o número {} e você o {}!\033[m'.format(aleatorio, num))
print('\033[1;33m====== Fim do jogo ======\033[m')
