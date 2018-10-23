for i in range(1, 101):  # Não há chaves {}
    if i % 15 == 0:      # Não é necessário parêntesis para a condição do if
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:     # elif combina 'else' com 'if'
        print("Buzz")
    else:
        print(i)
