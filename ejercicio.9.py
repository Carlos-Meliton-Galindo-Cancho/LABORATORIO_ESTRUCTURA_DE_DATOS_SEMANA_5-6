"""
EJERCICIO 9:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que tienen una longitud determinada

"""


def longitud_palabra(palabras, longitud=10):
    palabras_diez_a_mas_longitud = set()
    for palabra in palabras:
        if len(palabra) >= longitud:
            palabras_diez_a_mas_longitud.add(palabra)
    return palabras_diez_a_mas_longitud


conjunto_palabras = {'hola mundo', 'programacion', 'naranja', 'negro'}
print(longitud_palabra(conjunto_palabras))