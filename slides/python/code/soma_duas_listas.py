def soma_listas(l1, l2):
    saida = []
    for i, j in zip(l1, l2):
        saida.append(i+j)
    return saida


def soma_listas2(l1, l2):
    return [i+j for i, j in zip(l1, l2)]
