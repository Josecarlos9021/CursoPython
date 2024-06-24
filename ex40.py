print('====== Cáculo de média ======')
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
if  media < 5:
    print('Quem tirou {} e {} tem sua média \033[33m{:.1f}\033[m e você está \033[31mREPROVADO!\033[m'.format(nota1, nota2, media))
elif media >= 5 and media <= 7:
    print('Quem tirou {} e {} tem sua média \033[33m{:.1f}\033[m e você está em \033[34mRECUPERAÇÃO!\033[m'.format(nota1, nota2, media))
elif media >= 7:
    print('Quem tirou {} e {} tem sua média \033[33m{:.1f}\033[m e você está \033[32mAPROVADO!\033[m'.format(nota1, nota2, media))
