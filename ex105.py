def notas(*n, sit=False):
    """
    => Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações a situação turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situacao'] = 'BOA'
        elif r['média'] >= 5:
            r['situacao'] = 'Razoável'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(10, 6, 9.5, 8.5, sit=True)
print(resp)
help(notas)