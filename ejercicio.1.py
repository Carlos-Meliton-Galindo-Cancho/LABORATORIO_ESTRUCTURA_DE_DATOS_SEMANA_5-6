"""
EJERCICIO 1:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números primos

"""



def mi_funcion(numeros):                                          # se define una función llamada mi_funcion que toma un conjunto de números como entrada
    numeros_primos = set()                                        # se inicializa un conjunto vacío donde se almacenarán los números primos encontrados
    for numero in numeros:                                        # se itera a través de cada número en el conjunto dado
        n_divisores = 0
        for divisores in range(1, numero+1):                      # para cada número se itera a través de todos los enteros desde 1 hasta el número mismo (numero)
            if numero % divisores == 0:                        
                n_divisores += 1
        if n_divisores == 2:
            numeros_primos.add(numero)                            # si el número tiene exactamente dos divisores (1 y el propio número), se agrega a numeros_primos
    return numeros_primos                                     

conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}                # se define un conjunto de números conjunto_numeros
print(mi_funcion(conjunto_numeros))                               # se llama a la función con este conjunto y se imprime el resultado



"""

LA IMPRESION FINAL SERÁ:

{2, 3, 5, 7}

"""