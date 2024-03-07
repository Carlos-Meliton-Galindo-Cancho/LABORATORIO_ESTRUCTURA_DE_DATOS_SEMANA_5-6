"""
EJERCICIO 12:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están ordenados de mayor a menor

"""



def ordenar_conjunto_de_mayor_a_menor(conjunto):
    
    numeros_ordenados = sorted(conjunto, reverse=True)
    
    return numeros_ordenados

conjunto = {5, 2, 8, 1, 7}
print(ordenar_conjunto_de_mayor_a_menor(conjunto))

