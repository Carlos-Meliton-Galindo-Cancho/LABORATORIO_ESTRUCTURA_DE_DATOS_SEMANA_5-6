"""
EJERCICIO 17:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que tienen una longitud determinada y están ordenadas de menor a mayor

"""


def palabras_ordenadas(conjunto_palabras, longitud):                    # se define una función que toma dos argumentos: conjunto_palabras y longitud
    conjunto_palabras_ordenadas = set()                                 # se inicializa un conjunto vacío que contendrá las palabras que cumplen con la longitud mínima especificada
    for palabra in conjunto_palabras:                                   # este bucle for itera sobre cada palabra en el conjunto de palabras dado
        if len(palabra) >= longitud:                                    # se comprueba si la longitud de la palabra es mayor o igual a la longitud mínima especificada
            conjunto_palabras_ordenadas.add(palabra)                    # si la longitud de la palabra cumple con el requisito, se agrega al conjunto
    return sorted(conjunto_palabras_ordenadas)                          # finalmente la función devuelve una lista ordenada de las palabras que tienen una longitud igual o mayor que la longitud especificada y la función sorted() se utiliza para ordenar el conjunto de palabras

palabras = {"Python", "Programación", "lapiz",
            "Conjunto", "Ejemplo", "Palabra", "hola"}                   # aquí se crea un conjunto de palabras

print(palabras_ordenadas(palabras, 7))                                  # se llama a la función pasando este conjunto y el valor 7 como argumentos y el resultado se imprime en la consola



"""

LA IMPRESION FINAL SERÁ:

['Conjunto', 'Ejemplo', 'Palabra', 'Programación']

"""


