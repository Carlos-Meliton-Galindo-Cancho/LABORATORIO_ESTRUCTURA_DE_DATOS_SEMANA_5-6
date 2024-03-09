"""
EJERCICIO 10:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada

"""



def palabras_con_letra(conjunto_palabras, letra):                             # se define una función llamada palabras_con_letra que toma dos argumentos: conjunto_palabras y letra
    palabras_filtradas=set()                                                  # se inicializa un conjunto vacío que contendrá las palabras que contienen la letra especificada
    for palabra in conjunto_palabras:                                         # itera sobre cada palabra en el conjunto de palabras dado
        if letra in palabra:                                                  # se comprueba si la letra especificada está presente en la palabra actual
            palabras_filtradas.add(palabra)                                   # si la palabra contiene la letra especificada, se agrega al conjunto 
    return palabras_filtradas                                                 # finalmente la función devuelve el conjunto que contiene todas las palabras del conjunto original que contienen la letra especificada

conjunto_palabras = {"python", "java", "javascript", "ruby", "csharp"}        # aquí se crea un conjunto
letra = "a"

print(palabras_con_letra(conjunto_palabras, letra))                           # se llama a la función pasando este conjunto y la letra "a" como argumentos y el resultado se imprime en la consola



"""

LA IMPRESION FINAL SERÁ:

{'java', 'javascript', 'csharp'}

"""