'''
Para usar map() con diccionarios, podemos aplicar una función a los valores de un diccionario y obtener los resultados como un nuevo diccionario. 
La idea es aplicar una función a cada valor del diccionario y mantener las claves intactas. 
En Python, podemos lograr esto mediante la combinación de map() con un diccionario por comprensión o con la función dict().'''

# Veamos un ejemplo para entender cómo usar map() con diccionarios:

def doble(numero):
    return numero * 2

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Usando map() con un diccionario por comprensión
doble_numeros = {clave: doble(valor) for clave, valor in numeros.items()}

# Usando map() con la función dict()
doble_numeros2 = dict(map(lambda item: (item[0], doble(item[1])), numeros.items()))

print(doble_numeros)   # Salida: {'a': 2, 'b': 4, 'c': 6, 'd': 8}
print(doble_numeros2)  # Salida: {'a': 2, 'b': 4, 'c': 6, 'd': 8}

'''
n el primer caso, utilizamos una comprensión de diccionario para iterar sobre los elementos del diccionario numeros. 
En cada iteración, aplicamos la función doble() al valor del diccionario y creamos un nuevo diccionario con las claves originales y los valores duplicados.

En el segundo caso, utilizamos map() junto con la función dict() para lograr el mismo resultado. 
Usamos la función lambda para aplicar la función doble() a cada valor del diccionario y luego convertimos los resultados a un 
diccionario con dict().

Ambos enfoques son equivalentes y nos permiten aplicar una función a los valores de un diccionario y obtener un nuevo diccionario con los resultados.'''