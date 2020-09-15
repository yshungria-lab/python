<code>

# Para modificar
# el limite de recursividad
# simplemente importamos la librería sys

import sys
sys.setrecursionlimit(2000)


def factorial(n):
    """
    Calcula el factorial de n.
    n int > 0
    return n!
    """
    print(n)
    if n == 1:
        return 1
    else:
        return (n * factorial(n - 1))


n = int(input('Ingresa el numero que deseas calcular el factorial: '))
print(factorial(n))
# help(factorial)
