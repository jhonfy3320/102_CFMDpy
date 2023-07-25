'''En Dictionary Comprehension, la condición es una expresión opcional que se utiliza para filtrar elementos antes de incluirlos en el 
diccionario resultante. 
La condición se coloca después de la expresión que define la clave y el valor del elemento del nuevo diccionario.'''

## La sintaxis general de Dictionary Comprehension con una condición es la siguiente:

'''nuevo_diccionario = {clave_expresion: valor_expresion for elemento in iterable if condicion}
condicion es una expresión booleana que se evalúa para cada elemento del iterable. Si la condición es verdadera (True), 
el elemento se incluye en el nuevo diccionario; si es falsa (False), el elemento se omite y no se agrega al diccionario resultante.
Aquí tienes algunos ejemplos para ilustrar cómo funciona la condición en Dictionary Comprehension:'''

#Filtrar un diccionario y eliminar elementos que no cumplen cierta condición:

puntajes = {'Alice': 85, 'Bob': 70, 'Charlie': 95, 'David': 60}
mejores_puntajes = {nombre: puntaje for nombre, puntaje in puntajes.items() if puntaje >= 80}
print(mejores_puntajes)  # Salida: {'Alice': 85, 'Charlie': 95}

'''En este ejemplo, se utiliza la condición if puntaje >= 80 para filtrar el diccionario puntajes. Solo los elementos cuyos valores 
de puntaje sean mayores o iguales a 80 se incluirán en el nuevo diccionario mejores_puntajes.'''

## Filtrar y transformar un diccionario existente:

estudiantes = {'Alice': 85, 'Bob': 70, 'Charlie': 95, 'David': 60}
estudiantes_aprobados = {nombre: 'Aprobado' if nota >= 70 else 'Reprobado' for nombre, nota in estudiantes.items()}
print(estudiantes_aprobados)  # Salida: {'Alice': 'Aprobado', 'Bob': 'Aprobado', 'Charlie': 'Aprobado', 'David': 'Reprobado'}

'''En este ejemplo, la condición if nota >= 70 else 'Reprobado' se utiliza para asignar el valor 'Aprobado' a los estudiantes con una nota 
mayor o igual a 70, y el valor 'Reprobado' a los estudiantes con una nota inferior a 70.

La condición en Dictionary Comprehension es una herramienta poderosa que permite filtrar y transformar elementos de manera concisa en un 
diccionario. Permite personalizar qué elementos se incluyen en el nuevo diccionario en función de condiciones específicas.'''