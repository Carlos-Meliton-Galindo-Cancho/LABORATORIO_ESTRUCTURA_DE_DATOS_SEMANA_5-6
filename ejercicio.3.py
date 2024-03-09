"""
EJERCICIO 3:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que son divisibles por un número determinado

"""


def si_es_divisible(numeros, divisor):                                      # se define una función llamada si_es_divisible que toma dos argumentos: numeros y divisor
    divisibles = set()                                                      # se inicializa un conjunto vacío llamado donde se almacenarán los números del conjunto original que son divisibles por el divisor proporcionado
    for numero in numeros:                                                  # se itera a través de cada número en el conjunto de números dado
        if numero % divisor == 0:
            divisibles.add(numero)                                          # si el número es divisible por el divisor proporcionado (es decir, si el resto de la división es cero), se agrega al conjunto
    return divisibles                                                       # se devuelve el conjunto divisibles que contiene los números del conjunto original que son divisibles por el divisor proporcionado

conjunto_numeros = {1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 18}
print(si_es_divisible(conjunto_numeros, 6))                                 # luego se llama a la función si_es_divisible con ese conjunto de numeros y se imprime el resultado



"""

LA IMPRESION FINAL SERÁ:

{18, 12, 6}

"""










