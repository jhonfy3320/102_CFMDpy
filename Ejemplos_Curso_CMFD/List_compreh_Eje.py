'''List Comprehension es una forma concisa y elegante de crear listas en Python. 
Permite crear una nueva lista basada en otra lista existente o en un iterable, aplicando transformaciones y filtrando elementos 
según determinadas condiciones.

La sintaxis básica de Comprensión de listas es la siguiente:'''

## nueva_lista = [expresion for elemento in iterable if condicion]

'''nueva_listaes la lista creada a partir de List Comprehension.
expresiones la transformación o cálculo que se realiza en cada elemento del iterable para construir los elementos de la nueva lista.
elementoes una variable que toma cada valor del iterable en cada iteración.
iterablees una secuencia o colección de elementos como una lista, una cadena de texto, un rango, entre otros.
condiciones una expresión opcional que se utiliza para filtrar elementos según ciertas condiciones. 
Solo los elementos que cumplieron la condición se obtuvieron en la nueva lista.
Aquí tienes algunos ejemplos de Comprensión de listas para ilustrar su uso:'''

## Crear una lista de los cuadrados de los números del 1 al 5:

cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

## Filtrar los números pares de una lista:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # Salida: [2, 4, 6, 8, 10]

## Crear una lista de las primeras letras de una lista de palabras:

palabras = ['Python', 'es', 'genial']
primeras_letras = [palabra[0] for palabra in palabras]
print(primeras_letras)  # Salida: ['P', 'e', 'g']

## Filtrar y transformar una lista de números:

numeros = [-1, 2, -3, 4, -5]
positivos_cuadrados = [x**2 for x in numeros if x > 0]
print(positivos_cuadrados)  # Salida: [4, 16]

'''List Comprehension es una forma poderosa y compacta de crear listas en Python, permitiendo combinar transformaciones y filtrados en una sola expresión. 
Su uso puede hacer que el código sea más legible y conciso.'''