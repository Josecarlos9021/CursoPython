from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: º'))
rad = radians(ang)
seno = sin(rad)
cos = cos(rad)
tan = tan(rad)
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, cos))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ang, tan))
