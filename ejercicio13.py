"""
EJERCICIO 13:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están duplicados

"""


def n_duplicados(conjunto):
    lista = conjunto

    duplicados = []
    for i in lista:
        contar = lista.count(i)
        if contar == 2:
            duplicados.append(i)
    print(set(duplicados))


numeros = [1, 1, 2, 3, 4, 5, 4, 8, 2, 7, 9]
n_duplicados(numeros)