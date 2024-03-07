"""
EJERCICIO 3:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que son divisibles por un número determinado

"""


def si_es_divisible(numeros, divisor):
    divisibles = set()
    for numero in numeros:
        if numero % divisor == 0:
            divisibles.add(numero)

    return divisibles


conjunto_numeros = {1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 18}
print(si_es_divisible(conjunto_numeros, 6))