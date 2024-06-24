print('====== Cálculo de IMC ======')
peso = float(input('Digite seu peso: KG'))
altura = float(input('Digite a sua altura: '))
imc = peso / altura**2

if imc < 18.5:
    print('Seu IMC é {:.1f} e você está abaixo do peso.'.format(imc))
elif imc < 25:
    print('Seu IMC é {:.1f} e você está com o peso ideal.'.format(imc))
elif imc < 30:
    print('Seu IMC é {:.1f} e você está com sobrepeso.'.format(imc))
elif imc < 40:
    print('Seu IMC é {:.1f} e você está com obesidade.'.format(imc))
else:
    print('Seu IMC é {:.1f} e você está com obesidade mórbida.'.format(imc))
print('====== Cuide-se! ======')