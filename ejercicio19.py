"""
EJERCICIO 19:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de menor a mayor y que no están duplicados

"""


def no_duplicados(conjunto):
    no_duplicados = []
    for i in conjunto:
        contar = conjunto.count(i)
        if contar == 1:
            no_duplicados.append(i)
    print(set(no_duplicados))


numeros = [1, 1, 2, 3, 4, 5, 4, 8, 2, 7, 9]
no_duplicados(numeros)