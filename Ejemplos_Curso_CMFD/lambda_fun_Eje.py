
'''Las funciones anónimas en Python se crean utilizando la palabra clave lambda. 
A diferencia de las funciones definidas con def, las funciones lambda son funciones pequeñas y anónimas que pueden tener solo una expresión. 
Estas funciones son útiles cuando necesitas funciones simples que se pueden definir en una sola línea y no necesitan un nombre.'''

## La sintaxis básica de una función lambda es la siguiente:

'''
lambda argumentos: expresion
Ejemplo de una función lambda que devuelve el cuadrado de un número:'''

cuadrado = lambda x: x**2
print(cuadrado(5))  # Salida: 25

'''
En este ejemplo, definimos una función lambda que toma un argumento x y devuelve el cuadrado de x. 
a función lambda se asigna a la variable cuadrado y luego la llamamos pasando el valor 5, lo que resulta en la impresión de 25.

Las funciones lambda son útiles cuando se utilizan en conjunto con funciones que esperan funciones como argumentos, como map(), filter() o reduce(). 
Esto permite crear funciones pequeñas y específicas directamente en el lugar donde las necesitas, sin tener que definir una función con def.'''

## Ejemplo utilizando map() con función lambda:

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

'''En este ejemplo, utilizamos map() para aplicar la función lambda que calcula el cuadrado de cada elemento de la lista numeros. 
El resultado se almacena en la lista cuadrados.

Recuerda que aunque las funciones lambda son útiles para casos simples y cortos, para funciones más complejas y con múltiples expresiones, 
es recomendable utilizar funciones definidas con def para hacer el código más legible y mantenible.'''