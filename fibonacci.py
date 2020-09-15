# Este algoritmo es un ejemplo claro de recursividad.
# próximamente mostraré el algoritmo de uan manera optimizada y as eficiente.
def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


n = int((input('Ingrese el numero de meses: ')))
print(fibonacci(n))
