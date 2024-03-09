"""
EJERCICIO 7:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son anagramas

"""



def encontrar_anagramas(conjunto_palabras):                                     # se define la función encontrar_anagramas toma un conjunto de palabras conjunto_palabras como entrada
    anagramas = set()                                                           # se crea un conjunto vacío llamado anagramas para almacenar las palabras que son anagramas

    palabras_ordenadas = {}                                                     # se crea un diccionario que será utilizado para almacenar las palabras ordenadas como claves y una lista de palabras como valor

    for palabra in conjunto_palabras:                                           # se itera sobre cada palabra en el conjunto de palabras dado
        palabra_ordenada = ''.join(sorted(palabra))                             # luego se ordenan las letras de cada palabra y se concatenan nuevamente en una cadena

        if palabra_ordenada in palabras_ordenadas:                              # se verifica si la palabra ordenada ya está presente en el diccionario
            palabras_ordenadas[palabra_ordenada].append(palabra)                # si ya está, se agrega la palabra actual a la lista de palabras correspondiente
        else:
            palabras_ordenadas[palabra_ordenada] = [palabra]                    # si no está, se crea una nueva entrada en el diccionario con la palabra ordenada como clave y una lista que contiene la palabra actual como valor

    for palabras in palabras_ordenadas.values():                                # se itera sobre los valores del diccionario
        if len(palabras) > 1:                                                   # si alguna de las listas de palabras contiene más de una palabra, significa que hay anagramas presentes
            anagramas.update(palabras)                                          # en ese caso, se agregan todas las palabras de esa lista al conjunto de anagramas (anagramas) utilizando el método update
    return anagramas                                                            # finalmente, se devuelve el conjunto de palabras que son anagramas entre sí

conjunto_palabras = {"arroz", "zorra", "zarro", "perro", "carro"}
anagramas = encontrar_anagramas(conjunto_palabras)                              # se crea un conjunto de palabras y luego llama a la función encontrar_anagramas() con ese conjunto como argumento
print(anagramas)


"""

LA IMPRESION FINAL SERÁ:

{'zorra', 'arroz', 'zarro'}

"""