
"""
EJERCICIO 19:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de menor a mayor y que no están duplicados

"""


def no_duplicados(conjunto):                              # se define una función que toma un conjunto de números como argumento
    no_duplicados = []                                    # se inicializa un conjunto vacío que contendrá los números que no están duplicados
    for i in conjunto:                                    # se itera sobre cada elemento en el conjunto dado
        contar = conjunto.count(i)
        if contar == 1:                                   # se comprueba si el número aparece solo una vez en el conjunto
            no_duplicados.append(i)                       # si el número no está duplicado, se agrega al conjunto
    print(set(no_duplicados))

numeros = [1, 1, 2, 3, 4, 5, 4, 8, 2, 7, 9]               # se define un conjunto con algunos números duplicados
no_duplicados(numeros)                                    # se llama a la función pasando este conjunto como argumento. La función imprime los números que no están duplicados encontrados en el conjunto




"""

LA IMPRESION FINAL SERÁ:

{3, 5, 7, 8, 9}

"""

