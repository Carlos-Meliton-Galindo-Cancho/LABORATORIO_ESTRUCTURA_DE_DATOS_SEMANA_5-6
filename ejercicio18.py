"""
EJERCICIO 18:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada y están ordenadas de mayor a menor

"""



def filtrar_y_ordenar(conjunto_palabras, letra):                                 # se define una función que toma dos argumentos: conjunto_palabras y letra
    palabras_filtradas = set()                                                   # se inicializa un conjunto vacío que contendrá las palabras que contienen la letra especificada

    for palabra in conjunto_palabras:                                            # este bucle for itera sobre cada palabra en el conjunto de palabras dado
        if letra in palabra:                                                     # se verifica si la letra especificada está presente en la palabra actual
            palabras_filtradas.add(palabra)                                      # si la letra está presente la palabra se agrega al conjunto

    palabras_ordenadas = sorted(palabras_filtradas, key=len, reverse=True)       # se ordenan en orden descendente según su longitud utilizando la función sorted(). La palabra más larga aparecerá primero debido al parámetro key=len y reverse=True (que indica que se desea ordenar de mayor a menor longitud)
    return palabras_ordenadas                                                    # la función devuelve una lista ordenada de las palabras
    
conjunto_palabras = {"python", "programacion", "palabra", "sol", "hola"}         # se define un conjunto de palabras
letra = "a"

print(filtrar_y_ordenar(conjunto_palabras, letra))                               # se llama a la función pasando este conjunto y la letra "a" como argumentos y el resultado se imprime en la consola




"""

LA IMPRESION FINAL SERÁ:

['programacion', 'palabra', 'hola']

"""

