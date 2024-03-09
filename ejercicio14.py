"""
EJERCICIO 14:   Conjuntos

Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que no están duplicados

"""



def no_duplicados(conjunto):                                     # esta función recibe un conjunto de números como argumento
    
    no_duplicados = []                                           # se crea una lista vacía que almacenará los números que no están duplicados encontrados en el conjunto
    for i in conjunto:                                           # se itera sobre cada elemento en el conjunto
        contar_ocurrencias = conjunto.count(i)                   # se cuenta cuántas veces aparece cada elemento en el conjunto usando conjunto.count(i)
        if contar_ocurrencias == 1:       
            no_duplicados.append(i)                              # si un elemento aparece exactamente una vez, se considera no duplicado y se agrega a la lista no_duplicados
    print(set(no_duplicados))                                    # finalmente se imprime un conjunto formado por los números que no están duplicados. Se utiliza set() para eliminar duplicados adicionales que puedan estar presentes en la lista

numeros= [1, 1, 2, 3, 4, 5, 4, 8, 2, 7, 9]                       # se define una lista con algunos números duplicados
no_duplicados(numeros)                                           # luego se llama a la función pasando esta lista como argumento. La función imprime los números que no están duplicados encontrados en la lista



"""

LA IMPRESION FINAL SERÁ:

{3, 5, 7, 8, 9}

"""


