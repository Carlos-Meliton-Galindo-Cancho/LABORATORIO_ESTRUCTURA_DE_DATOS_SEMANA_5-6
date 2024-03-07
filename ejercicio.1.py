"""
EJERCICIO 1:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números primos

"""



def mi_funcion(numeros):
    numeros_primos = set()
    for numero in numeros:
        n_divisores = 0
        for divisores in range(1, numero+1):
            if numero % divisores == 0:
                n_divisores += 1
        if n_divisores == 2:
            numeros_primos.add(numero)
    return numeros_primos


conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(mi_funcion(conjunto_numeros))