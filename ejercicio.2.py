"""
EJERCICIO 2:   Conjuntos

Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que comienzan con una letra determinada

"""



def palabras_comienzan_con_la_letra(conjunto_palabras, letra_inicial):                     # se define una función llamada palabras_comienzan_con_la_letra que toma dos argumentos: conjunto_palabras y letra_inicial                      
    palabras_filtradas= set()                                                              # se inicializa un conjunto vacío donde se almacenarán las palabras que comienzan con la letra inicial proporcionada
    for palabra in conjunto_palabras:                                                      # se itera a través de cada palabra en el conjunto de palabras dado
        if palabra.startswith(letra_inicial):
            palabras_filtradas.add(palabra)                                                # si la palabra comienza con la letra inicial proporcionada, se agrega al conjunto palabras_filtradas
    return palabras_filtradas                                                              # se retorna el conjunto de palabras filtradas

conjunto_palabras = {"python", "java", "javascript", "html", "css"}                        # se define un conjunto de palabras y una letra inicial                                   
letra_inicial = "j"
print(palabras_comienzan_con_la_letra(conjunto_palabras, letra_inicial))                   # se llama a la función palabras_comienzan_con_la_letra con estos argumentos y se imprime el resultado




"""

LA IMPRESION FINAL SERÁ:

{'java', 'javascript'}

"""






