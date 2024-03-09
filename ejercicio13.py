"""
EJERCICIO 13:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están duplicados

"""


def n_duplicados(conjunto):                                       # esta función recibe un conjunto de números como argumento
    lista = conjunto                                              # aquí se asigna el conjunto recibido a una lista

    duplicados = []                                               # se crea una lista vacía que almacenará los números duplicados encontrados en el conjunto
    for i in lista:                                               # se itera sobre cada elemento en la lista
        contar = lista.count(i)                                   # se cuenta cuántas veces aparece cada elemento en la lista usando lista.count(i)
        if contar == 2:
            duplicados.append(i)                                  # si un elemento aparece exactamente dos veces, se considera duplicado y se agrega a la lista duplicados
    print(set(duplicados))                                        # finalmente se imprime un conjunto formado por los números duplicados encontrados. Se utiliza set() para eliminar duplicados adicionales que puedan estar presentes en la lista

numeros = [1, 1, 2, 3, 4, 5, 4, 8, 2, 7, 9]                       # se define una lista con algunos números duplicados  
n_duplicados(numeros)                                             # luego se llama a la función pasando esta lista como argumento. La función imprime los números duplicados encontrados en la lista




"""

LA IMPRESION FINAL SERÁ:

{1, 2, 4}

"""





