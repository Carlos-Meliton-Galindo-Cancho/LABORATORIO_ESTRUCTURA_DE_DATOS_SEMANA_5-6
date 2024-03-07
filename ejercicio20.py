"""
EJERCICIO 20:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor

"""




def filtrar_palindromos_por_longitud(conjunto_palabras, longitud):
    palindromos_filtrados = set()

    for palabra in conjunto_palabras:
        
        if palabra == palabra[::-1] and len(palabra) == longitud:
            palindromos_filtrados.add(palabra)

    palindromos_ordenados = sorted(palindromos_filtrados, key=len)

    return set(palindromos_ordenados)

conjunto_palabras = {"level", "radar", "python", "deed", "noon"}
longitud = 4
print(filtrar_palindromos_por_longitud(conjunto_palabras, longitud))

