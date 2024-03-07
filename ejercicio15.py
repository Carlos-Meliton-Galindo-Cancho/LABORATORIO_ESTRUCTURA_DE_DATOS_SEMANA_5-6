"""
EJERCICIO 15:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que son primos y están ordenados de menor a mayor

"""


def numero_primos_ordenados(numeros):

    numeros_primos_y_ordenados = set()
    for numero in numeros:
        divisores = 0
        for i in range(1, numero+1):
            if numero % i == 0:
                divisores += 1
        if divisores == 2:
            numeros_primos_y_ordenados.add(numero)

    print(numeros_primos_y_ordenados)


conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9}

numero_primos_ordenados(conjunto_numeros)