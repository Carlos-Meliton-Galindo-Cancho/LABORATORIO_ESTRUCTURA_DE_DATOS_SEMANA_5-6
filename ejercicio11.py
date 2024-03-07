"""
EJERCICIO 11:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de menor a mayor

"""


def conjunto_ordenado(conjunto):

    conjunto_ordenado = sorted(list(conjunto))
    return set(conjunto_ordenado)


conjunto = {1, 5, 2, 6, 4, 3}
print(conjunto_ordenado(conjunto))