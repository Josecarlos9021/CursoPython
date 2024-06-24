def leiaDinheiro(mensagem):
    válido = False
    while not válido:
        num = str(input(mensagem)).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print(f'\033[1;31mErro! \"{num}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(num)