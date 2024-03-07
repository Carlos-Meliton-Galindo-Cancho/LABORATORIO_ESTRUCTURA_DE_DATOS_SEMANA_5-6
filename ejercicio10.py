"""
EJERCICIO 10:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada

"""




def palabras_con_letra(conjunto_palabras, letra):
    palabras_filtradas=set()
    for palabra in conjunto_palabras:
        if letra in palabra:
            palabras_filtradas.add(palabra)
    return palabras_filtradas

conjunto_palabras = {"python", "java", "javascript", "ruby", "csharp"}
letra = "a"

print(palabras_con_letra(conjunto_palabras, letra))

