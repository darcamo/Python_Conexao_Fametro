def my_func(a, b, *args, **kwargs):  # 'a' é um 'b' são parâmetros obrigatórios
    print(a)
    print(b)
    # tupla de todos os parâmetros via posição
    print(args)

    # Dicionário com todos os parâmetros fornecidos via palavra chave
    print(kwargs)
