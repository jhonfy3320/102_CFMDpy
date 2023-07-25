'''
Para filtrar diccionarios en Python, puedes utilizar comprensiones de diccionarios o la función filter() en combinación con una función lambda. 
A continuación, te mostraré ambos enfoques:

Supongamos que tienes un diccionario con información de personas y quieres filtrar aquellos que sean mayores de 18 años.'''

## Usando comprensiones de diccionarios:

personas = {
    'Alice': 25,
    'Bob': 17,
    'Charlie': 30,
    'David': 19,
    'Eve': 22
}

# Filtrar las personas mayores de 18 años usando una comprensión de diccionario
personas_mayores = {nombre: edad for nombre, edad in personas.items() if edad > 18}

print(personas_mayores)  # Salida: {'Alice': 25, 'Charlie': 30, 'David': 19, 'Eve': 22}

'''
En este ejemplo, utilizamos una comprensión de diccionario para filtrar las personas mayores de 18 años. 
La expresión {nombre: edad for nombre, edad in personas.items() if edad > 18} crea un nuevo diccionario que 
contiene solo aquellos pares clave-valor cuya edad es mayor a 18.'''

## Usando filter() con función lambda:

personas = {
    'Alice': 25,
    'Bob': 17,
    'Charlie': 30,
    'David': 19,
    'Eve': 22
}

# Función lambda que devuelve True si la edad es mayor a 18
es_mayor_de_edad = lambda edad: edad > 18

# Filtrar las personas mayores de 18 años usando filter() y la función lambda
personas_mayores = dict(filter(lambda item: es_mayor_de_edad(item[1]), personas.items()))

print(personas_mayores)  # Salida: {'Alice': 25, 'Charlie': 30, 'David': 19, 'Eve': 22}

'''
En este ejemplo, definimos una función lambda es_mayor_de_edad que toma una edad como argumento y devuelve True si la edad es mayor a 18.

Luego, utilizamos filter() junto con la función lambda y dict() para filtrar las personas mayores de 18 años. 
La expresión filter(lambda item: es_mayor_de_edad(item[1]), personas.items()) devuelve un objeto filter con los pares 
clave-valor que cumplen la condición de ser mayores de 18. Finalmente, convertimos el objeto filter a un diccionario usando dict() 
para obtener el resultado deseado.

Ambos enfoques nos permiten filtrar los elementos de un diccionario basándonos en una condición específica, lo que puede ser útil para 
seleccionar información relevante en determinadas situaciones.'''