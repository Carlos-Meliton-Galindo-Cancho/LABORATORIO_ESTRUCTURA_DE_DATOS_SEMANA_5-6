"""
EJERCICIO 16:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos y están ordenadas de menor a mayor

"""



def palindromos_ordenados(conjunto_palabras):                                     # se define una función que toma un conjunto de palabras como argumento
    palindromos = set()                                                           # se inicializa un conjunto vacío que contendrá las palabras palíndromas encontradas en el conjunto dado
    
    for palabra in conjunto_palabras:                                             # este bucle for itera sobre cada palabra en el conjunto de palabras dado
        if palabra == palabra[::-1]:                                              # dentro del bucle se verifica si la palabra es un palíndromo. Compara la palabra con su inversa (palabra[::-1]). Si la palabra es igual a su inversa, significa que es un palíndromo
            palindromos.add(palabra)                                              # si la palabra es un palíndromo se agrega al conjunto palindromos
    
    palindromos_ordenados = sorted(palindromos, key=len)                          # después de encontrar todos los palíndromos, se ordenan en orden ascendente según su longitud utilizando la función sorted(). La palabra más corta aparecerá primero debido al parámetro key=len, que especifica que la longitud de cada palabra debe usarse como criterio de ordenamiento
    return palindromos_ordenados                                                  # la función devuelve la lista de palabras palíndromas ordenadas de menor a mayor longitud

conjunto_palabras = {"oso", "casa", "radar", "nivel", "python", "reconocer"}      # se define un conjunto de palabras
print(palindromos_ordenados(conjunto_palabras))                                   # se llama a la función pasando este conjunto como argumento. El resultado se imprime en la consola



"""

LA IMPRESION FINAL SERÁ:

['oso', 'radar', 'reconocer']

"""

