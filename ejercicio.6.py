"""
EJERCICIO 6:   Conjuntos

Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en el segundo conjunto pero no en el primero

"""



def diferencia_entre_conjuntos(conjunto1, conjunto2):                              # se define una función llamada diferencia_entre_conjuntos que toma dos conjuntos como parámetros de entrada: conjunto1 y conjunto2
    return conjunto2.difference(conjunto1)                                         # se utiliza el método difference() del conjunto conjunto2 para calcular la diferencia entre conjunto2 y conjunto1. Este método devuelve un nuevo conjunto que contiene los elementos que están en conjunto2 pero no en conjunto1

conjunto1 = {1, 2, 3, 4, 5}                                                        # se definen dos conjuntos, conjunto1 y conjunto2, con valores específicos
conjunto2 = {4, 5, 6, 7, 8}

print(diferencia_entre_conjuntos(conjunto1, conjunto2))                            # luego se llama a la función diferencia_entre_conjuntos con estos conjuntos como argumentos y se imprime el resultado



"""

LA IMPRESION FINAL SERÁ:

{8, 6, 7}

"""



