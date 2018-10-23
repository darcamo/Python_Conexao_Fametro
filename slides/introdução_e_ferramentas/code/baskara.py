import math  # Importa o módulo math
a = float(input("Entre com o coeficiente a\n: "))  # input recebe um valor do teclado
b = float(input("Entre com o coeficiente b\n: "))  # O valor retornado e uma string
c = float(input("Entre com o coeficiente c\n: "))  # Usamos float para converter
delta = b*b - 4*a*c
if delta >= 0:  # Se delta for negativo obtemos raízes complexas
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    # O método 'format' "formata" uma string substiruindo valores
    print("x1 = {0}\nx2 = {1}".format(x1, x2))
else:
    print("As raízes não são reais")
