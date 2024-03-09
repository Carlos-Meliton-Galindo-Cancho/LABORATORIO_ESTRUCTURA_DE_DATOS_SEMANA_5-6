"""
EJERCICIO 11:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de menor a mayor

"""


def conjunto_ordenado(conjunto):                                # se define una función que toma un conjunto de números como argumento

    conjunto_ordenado = sorted(list(conjunto))                  # el conjunto se convierte primero en una lista usando list(conjunto). Luego, esa lista se ordena usando la función sorted() (ordenará los elementos del conjunto de menor a mayor y los almacenará en la variable conjunto_ordenado)
    return set(conjunto_ordenado)                               # se devuelve un nuevo conjunto que contiene los elementos ordenados y set() se utiliza para convertir la lista ordenada nuevamente en un conjunto, eliminando cualquier duplicado que pueda haber surgido durante el proceso de ordenación


conjunto = {1, 5, 2, 6, 4, 3}                                   # aquí se define un conjunto con algunos números desordenados
print(conjunto_ordenado(conjunto))                              # luego se llama a la función pasando este conjunto como argumento y el resultado, que es un conjunto con los números ordenados de menor a mayor, se imprime en la consola




"""

LA IMPRESION FINAL SERÁ:

{1, 2, 3, 4, 5, 6}

"""
