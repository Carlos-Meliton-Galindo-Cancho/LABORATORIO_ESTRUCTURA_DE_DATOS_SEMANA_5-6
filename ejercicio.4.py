"""
EJERCICIO 4:   Conjuntos

Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en ambos conjuntos

"""


def interseccion_entre_conjuntos(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)


conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

print(interseccion_entre_conjuntos(conjunto1, conjunto2))


