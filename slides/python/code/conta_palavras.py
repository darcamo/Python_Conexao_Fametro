texto = '''"Onde fica a saída?", Perguntou Alice ao gato que ria.
"Depende", respondeu o gato.
"De quê?", replicou Alice;
"Depende de para onde você quer ir..."'''
palavras = texto.split()  # Separa o texto em uma lista de palavras
print("O texto tem {0} palavras, sendo {1} delas diferentes.".format(
    len(palavras),      # Número de palavras
    len(set(palavras))  # Número de palavras únicas
))
