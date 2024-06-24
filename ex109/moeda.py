def metade(preço, formatar=False):
    '''
        => Calcula o aumento de um determinado preço,
        retornando o resultado, com ou sem formatação.
        :param preço: o preço que se quer reajustar.
        :param taxa: qual é a porcentagem do aumento.
        :param formatar: quer a saída formatada ou não?
        :return: o valor reajustado, com ou sem formato.
    '''
    res = preço / 2
    return moeda(res) if formatar else res


def dobro(preço, formatar=False):
    res = preço * 2
    if formatar:
        return moeda(res)
    else:
        return res


def aumentar(preço, taxa, formatar=False):
    res = preço + (preço * taxa/100)
    return res if not formatar else moeda(res)


def diminuir(preço, taxa, formatar=False):
    res = preço - (preço * taxa/100)
    return res if formatar is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')