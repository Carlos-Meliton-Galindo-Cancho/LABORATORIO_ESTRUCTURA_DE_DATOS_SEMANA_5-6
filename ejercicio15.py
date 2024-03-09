"""
EJERCICIO 15:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que son primos y están ordenados de menor a mayor

"""


def numeros_primos_ordenados(numeros):                                # se define una función que toma un conjunto de números como argumento
    numeros_primos = set()                                            # se inicializa un conjunto vacío que contendrá los números primos encontrados en el conjunto dado

    for numero in numeros:                                            # se itera sobre cada número en el conjunto de números dado
        if numero > 1:                                                # se verifica si el número es mayor que 1, ya que 1 no se considera primo
            es_primo = True
            for i in range(2, numero):                                # se prueba si el número es divisible por algún otro número (desde 2 hasta el número - 1)
                if numero % i == 0:
                    es_primo = False                                  # si se encuentra un divisor, se marca es_primo como False y se rompe el bucle
                    break
            if es_primo:
                numeros_primos.add(numero)                            # si (es_primo es True) después del bucle, significa que el número es primo y se agrega al conjunto numeros_primos

    numeros_primos_ordenados = sorted(numeros_primos)                 # se ordenan los números primos encontrados y se devuelve la lista ordenada. sorted() se utiliza para garantizar que los números primos estén en orden ascendente
    return numeros_primos_ordenados

conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9}                        # se define un conjunto de números
print(numeros_primos_ordenados(conjunto_numeros))                     # se llama a la función pasando este conjunto como argumento. El resultado, que es una lista con los números primos ordenados de menor a mayor, se imprime en la consola



"""

LA IMPRESION FINAL SERÁ:

[2, 3, 5, 7]

"""

