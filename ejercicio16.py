"""
EJERCICIO 16:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos y están ordenadas de menor a mayor

"""



def palindromos_ordenados(conjunto_palabras):
    palindromos = set()
    
    for palabra in conjunto_palabras:
        if palabra == palabra[::-1]:
            palindromos.add(palabra)
    
    
    palindromos_ordenados = sorted(palindromos, key=len)
    
    return palindromos_ordenados


conjunto_palabras = {"oso", "casa", "radar", "nivel", "python", "reconocer"}
print(palindromos_ordenados(conjunto_palabras))

