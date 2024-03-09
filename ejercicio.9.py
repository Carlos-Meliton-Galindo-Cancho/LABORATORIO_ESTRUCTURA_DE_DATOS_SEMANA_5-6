"""
EJERCICIO 9:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que tienen una longitud determinada

"""


def longitud_palabra(palabras, longitud=10):                                   # se define una función llamada longitud_palabra que toma dos argumentos: palabras y longitud (por defecto, longitud está establecido en 10)
    palabras_diez_a_mas_longitud = set()                                       # se inicializa un conjunto vacío que contendrá las palabras que tienen una longitud igual o mayor que el valor especificado
    for palabra in palabras:                                                   # se itera sobre cada palabra en el conjunto de palabras dado 
        if len(palabra) >= longitud:                                           # se comprueba si la longitud de la palabra es mayor o igual a la longitud mínima especificada
            palabras_diez_a_mas_longitud.add(palabra)                          # si la longitud de la palabra cumple con el requisito, se agrega al conjunto
    return palabras_diez_a_mas_longitud                                        # finalmente la función devuelve el conjunto que contiene todas las palabras que tienen una longitud igual o mayor que la longitud especificada


conjunto_palabras = {'hola mundo', 'programacion', 'naranja', 'negro'}         # aquí se crea un conjunto de palabras
print(longitud_palabra(conjunto_palabras))                                     # se llama a la función pasando este conjunto como argumento y el resultado se imprime en la consola



"""

LA IMPRESION FINAL SERÁ:

{'hola mundo', 'programacion'}

"""