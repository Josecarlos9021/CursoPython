'''oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = oposto**2 + adjacente**2
resultado = hipotenusa ** (1/2)
print('O resultado da hipotenusa do valor cateto oposto {} e adjacente {} é {:.2f}'.format(oposto, adjacente, resultado))'''

import math
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
