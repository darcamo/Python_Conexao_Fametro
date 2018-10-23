N = int(input("Entre com N: "))
F = 1
N_original = N
while N >= 2:
    F = F * N
    N = N - 1
print("O fatorial de {0} vale {1}".format(N_original, F))
