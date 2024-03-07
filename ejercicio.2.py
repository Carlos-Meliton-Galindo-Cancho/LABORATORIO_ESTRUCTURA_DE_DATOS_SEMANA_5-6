"""
EJERCICIO 2:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que comienzan con una letra determinada

"""



def palabras_comienzan_con_la_letra(conjunto_palabras, letra_inicial):
    palabras_filtradas= set()
    for palabra in conjunto_palabras:
        if palabra.startswith(letra_inicial):
            palabras_filtradas.add(palabra)
    return palabras_filtradas

conjunto_palabras = {"python", "java", "javascript", "html", "css"}
letra_inicial = "j"
print(palabras_comienzan_con_la_letra(conjunto_palabras, letra_inicial))