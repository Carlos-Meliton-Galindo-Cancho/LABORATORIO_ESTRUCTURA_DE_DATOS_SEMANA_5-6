"""
EJERCICIO 17:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que tienen una longitud determinada y están ordenadas de menor a mayor

"""


def palabras_ordenadas(conjunto_palabras, longitud):
    conjunto_palabras_ordenadas = set()
    for palabra in conjunto_palabras:
        if len(palabra) >= longitud:
            conjunto_palabras_ordenadas.add(palabra)
    return sorted(conjunto_palabras_ordenadas)


palabras = {"Python", "Programación", "lapiz",
            "Conjunto", "Ejemplo", "Palabra", "hola"}

print(palabras_ordenadas(palabras, 7))