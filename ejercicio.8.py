"""
EJERCICIO 8:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos

"""



def palabras_palindromas(conjunto_palabras):                                # se define la función palabras_palindromas que toma un conjunto de palabras como entrada
    palindromas=set()                                                       # se crea un conjunto vacío para almacenar las palabras que son palíndromos

    for palabra in conjunto_palabras:                                       # se itera sobre cada palabra en el conjunto de palabras dado
        if palabra == palabra[::-1]:                                        # se compara cada palabra con su versión invertida (utilizando la técnica de slicing [::-1])
            palindromas.add(palabra)                                        # si la palabra original es igual a su versión invertida, significa que es un palíndromo y se agrega al conjunto de palíndromos
    return palindromas

conjunto_palabras = {"radar", "oso", "python", "level", "civic"}            # aquí se crea un conjunto de palabras

print(palabras_palindromas(conjunto_palabras))                              # se llama a la función palabras_palindromas pasando este conjunto como argumento y el resultado se imprime en la consola




"""

LA IMPRESION FINAL SERÁ:

{'level', 'civic', 'radar', 'oso'}

"""





