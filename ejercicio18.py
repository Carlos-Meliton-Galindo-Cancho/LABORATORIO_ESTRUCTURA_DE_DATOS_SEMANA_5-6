"""
EJERCICIO 18:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada y están ordenadas de mayor a menor

"""




def filtrar_y_ordenar(conjunto_palabras, letra):
    palabras_filtradas = set()

    for palabra in conjunto_palabras:
        if letra in palabra:
            palabras_filtradas.add(palabra)

    palabras_ordenadas = sorted(palabras_filtradas, key=len, reverse=True)

    return palabras_ordenadas
    

conjunto_palabras = {"python", "programacion", "palabra", "sol", "hola"}
letra = "a"

print(filtrar_y_ordenar(conjunto_palabras, letra))