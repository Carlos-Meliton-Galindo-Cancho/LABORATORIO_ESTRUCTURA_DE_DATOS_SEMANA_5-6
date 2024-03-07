"""
EJERCICIO 5:   Conjuntos

Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en el primer conjunto pero no en el segundo

"""


def diferencia_conjuntos(conjunto_1, conjunto_2):
    diferencia = conjunto_1.difference(conjunto_2)

    return diferencia


conjunto_1 = {1, 2, 3, 4, 5, 6}
conjunto_2 = {5, 6, 7, 8, 9, 10}

print(diferencia_conjuntos(conjunto_1, conjunto_2))