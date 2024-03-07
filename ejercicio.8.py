"""
EJERCICIO 8:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos

"""




def palabras_palindromas(conjunto_palabras):
    palindromas=set()
    for palabra in conjunto_palabras:
        if palabra == palabra[::-1]:
            palindromas.add(palabra)
    return palindromas

conjunto_palabras = {"radar", "oso", "python", "level", "civic"}

print(palabras_palindromas(conjunto_palabras))
