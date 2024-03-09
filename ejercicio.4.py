"""
EJERCICIO 4:   Conjuntos

Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en ambos conjuntos

"""


def interseccion_entre_conjuntos(conjunto1, conjunto2):                            # se define una función llamada interseccion_entre_conjuntos que toma dos conjuntos como entrada: conjunto1 y conjunto2
    return conjunto1.intersection(conjunto2)                                       # se utiliza el método intersection para calcular la intersección entre conjunto1 y conjunto2, que devuelve un conjunto que contiene los elementos presentes en ambos conjuntos

conjunto1 = {1, 2, 3, 4, 5}                                                        # se definen dos conjuntos, conjunto1 y conjunto2
conjunto2 = {4, 5, 6, 7, 8}

print(interseccion_entre_conjuntos(conjunto1, conjunto2))                          # luego se llama a la función con estos conjuntos como argumentos y se imprime el resultado




"""

LA IMPRESION FINAL SERÁ:

{4, 5}

"""