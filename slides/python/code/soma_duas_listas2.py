def soma_listas3(l1, l2):
    saida = [i+j for i, j in zip(l1, l2)]
    # Sabemos que o tamanho corresponde ao tamanho da menor
    # lista devido a como # a função zip funciona
    tamanho = len(saida)
    # Basta acrescentar os elementos restantes da lista maior
    saida.extend(l1[tamanho:])  # Notem que usamos extend e não append
    saida.extend(l2[tamanho:])
    return saida
