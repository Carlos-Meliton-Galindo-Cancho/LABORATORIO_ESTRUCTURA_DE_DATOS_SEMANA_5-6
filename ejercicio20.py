"""
EJERCICIO 20:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor

"""



def filtrar_palindromos_por_longitud(conjunto_palabras, longitud):                # se define una función que toma dos argumentos: conjunto_palabras y longitud
    palindromos_filtrados = set()                                                 # se inicializa un conjunto vacío que contendrá los palíndromos encontrados que tienen la longitud especificada

    for palabra in conjunto_palabras:                                             # este bucle for itera sobre cada palabra en el conjunto de palabras dado 
        if palabra == palabra[::-1] and len(palabra) == longitud:                 # se verifica si la palabra es un palíndromo (comparando la palabra con su inversa) y si su longitud es igual a la longitud especificada
            palindromos_filtrados.add(palabra)                                    # si ambas condiciones se cumplen, la palabra se agrega al conjunto palindromos_filtrados

    palindromos_ordenados = sorted(palindromos_filtrados, key=len)                # se ordenan en orden ascendente según su longitud utilizando la función sorted(). La palabra más corta aparecerá primero debido al parámetro key=len, que especifica que la longitud de cada palabra debe usarse como criterio de ordenamiento
    return set(palindromos_ordenados)                                             # la función devuelve un conjunto formado por los palíndromos

conjunto_palabras = {"level", "radar", "python", "deed", "noon"}                  # se define un conjunto de palabras 
longitud = 4

print(filtrar_palindromos_por_longitud(conjunto_palabras, longitud))              # luego se llama a la función pasando este conjunto y la longitud como argumentos y el resultado se imprime en la consola




"""

LA IMPRESION FINAL SERÁ:

{'deed', 'noon'}

"""

