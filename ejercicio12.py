"""
EJERCICIO 12:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de mayor a menor

"""



def ordenar_conjunto_de_mayor_a_menor(conjunto):                        # se define una función que toma un conjunto de números como argumento  
    numeros_ordenados = sorted(conjunto, reverse=True)                  # se utiliza la función sorted() para ordenar el conjunto de números de mayor a menor (reverse=True indica que se quiere el orden descendente) y los números ordenados se almacenan en la variable numeros_ordenados    
    return numeros_ordenados                                            # se devuelve una lista con los números ordenados de mayor a menor

conjunto = {5, 2, 8, 1, 7}                                              # aquí se define un conjunto con algunos números desordenados
print(ordenar_conjunto_de_mayor_a_menor(conjunto))                      # luego se llama a la función pasando este conjunto como argumento y el resultado, que es una lista con los números ordenados de mayor a menor, se imprime en la consola




"""

LA IMPRESION FINAL SERÁ:

[8, 7, 5, 2, 1]

"""