"""
EJERCICIO 5:   Conjuntos

Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en el primer conjunto pero no en el segundo

"""


def diferencia_conjuntos(conjunto_1, conjunto_2):                          # se define una función llamada diferencia_conjuntos que toma dos conjuntos como entrada: conjunto_1 y conjunto_2
    diferencia = conjunto_1.difference(conjunto_2)                         # se utiliza el método difference para calcular la diferencia entre conjunto_1 y conjunto_2, que devuelve un conjunto que contiene los elementos presentes en conjunto_1 pero no en conjunto_2
    return diferencia                                                      # se devuelve el conjunto diferencia que contiene los números que están en conjunto_1 pero no en conjunto_2

conjunto_1 = {1, 2, 3, 4, 5, 6}                                            # se definen dos conjuntos, conjunto_1 y conjunto_2
conjunto_2 = {5, 6, 7, 8, 9, 10}

print(diferencia_conjuntos(conjunto_1, conjunto_2))                        # luego se llama a la función diferencia_conjuntos con estos conjuntos como argumentos y se imprime el resultado




"""

LA IMPRESION FINAL SERÁ:

{1, 2, 3, 4}

"""


