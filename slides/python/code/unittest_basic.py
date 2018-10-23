import unittest

# Ao invés de definir fun aqui, nós também podemos importá-la de outro módulo
def fun(x):
    return x + 1

# Para criar novos casos de teste criamos uma subclasse de unittest.TestCase
class MyTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(fun(3), 4)


if __name__ == '__main__':
    # Automaticamente executa todos os métodos com nome "test_alguma_coisa" será executado
    unittest.main()
