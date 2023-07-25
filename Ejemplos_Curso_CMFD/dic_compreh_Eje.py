'''Dictionary Comprehension es una forma concisa y eficiente de crear diccionarios en Python. 
Permite construir un diccionario a partir de otro iterable, aplicando transformaciones y filtros según condiciones específicas. 
La sintaxis básica de Dictionary Comprehension es la siguiente:

nuevo_diccionario = {clave_expresion: valor_expresion for elemento in iterable if condicion}
nuevo_diccionarioes el diccionario creado mediante Dictionary Comprehension.
clave_expresiones la expresión que define la clave de cada elemento en el nuevo diccionario.
valor_expresiones la expresión que define el valor correspondiente a cada clave en el nuevo diccionario.
elementoes una variable que toma cada valor del iterable en cada iteración.
iterablees una secuencia o colección de elementos como una lista, una cadena de texto, un rango, entre otros.
condiciones una expresión opcional que se utiliza para filtrar elementos según ciertas condiciones. 
Solo los elementos que cumplieron la condición se obtuvieron en el nuevo diccionario.
'''
#Aquí tienes algunos ejemplos de Dictionary Comprehension para ilustrar su uso:

##Crear un diccionario con cuadrados de números del 1 al 5 como claves y los números como valores:

cuadrados = {x: x**2 for x in range(1, 6)}
print(cuadrados)  # Salida: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

##Filtrar un diccionario y eliminar elementos según cierta condición:

puntajes = {'Alice': 85, 'Bob': 70, 'Charlie': 95, 'David': 60}
mejores_puntajes = {nombre: puntaje for nombre, puntaje in puntajes.items() if puntaje >= 80}
print(mejores_puntajes)  # Salida: {'Alice': 85, 'Charlie': 95}

#Crear un diccionario a partir de una lista con claves y valores personalizados:

personas = ['Alice', 'Bob', 'Charlie']
edades = [25, 30, 35]
diccionario_personas = {persona: edad for persona, edad in zip(personas, edades)}
print(diccionario_personas)  # Salida: {'Alice': 25, 'Bob': 30, 'Charlie': 35}

##Filtrar y transformar un diccionario existente:

estudiantes = {'Alice': 85, 'Bob': 70, 'Charlie': 95, 'David': 60}
estudiantes_aprobados = {nombre: nota for nombre, nota in estudiantes.items() if nota >= 70}
print(estudiantes_aprobados)  # Salida: {'Alice': 85, 'Charlie': 95, 'Bob': 70}

'''Estos ejemplos demuestran cómo se puede utilizar Dictionary Comprehension para construir diccionarios de manera concisa y eficiente, 
aplicando transformaciones y filtros según sea necesario. 
Esta técnica es especialmente útil cuando se desea construir un diccionario de manera rápida y legible.'''