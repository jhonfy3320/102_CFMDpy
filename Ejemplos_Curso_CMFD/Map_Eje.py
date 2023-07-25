'''
La función map() en Python es una higher-order function que se utiliza para aplicar una función dada a cada elemento de un iterable 
(como una lista o tupla) y devuelve un nuevo iterable con los resultados. '''

## La sintaxis básica de la función map() es la siguiente:

'''
map(funcion, iterable)
funcion: Es la función que se aplicará a cada elemento del iterable.
iterable: Es el iterable (por ejemplo, una lista o tupla) sobre el cual se aplicará la función.
Veamos un ejemplo para entender mejor cómo funciona map():'''

def cuadrado(numero):
    return numero**3

numeros = [1, 2, 3, 4, 5]

# Usando la función map() para aplicar cuadrado a cada elemento de la lista
cuadrados = map(cuadrado, numeros)

# Convierte el resultado a una lista (en Python 2.x, esto no es necesario)
cuadrados = list(cuadrados)

print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

'''
En este ejemplo, definimos una función cuadrado que toma un número como argumento y devuelve su cuadrado. 
Luego, tenemos una lista llamada numeros con algunos números. 
Utilizamos la función map(cuadrado, numeros) para aplicar la función cuadrado a cada elemento de la lista numeros.'''

'''
El resultado de map() es un objeto map que es iterable. 
Para convertirlo a una lista con los resultados finales, utilizamos list(cuadrados).

Es importante mencionar que en Python 2.x, map() devuelve una lista directamente, pero en Python 3.x devuelve un objeto map. 
Por lo tanto, en Python 3.x, a menudo es necesario convertir el objeto map a una lista o a otra estructura de datos para ver los resultados.

La función map() es útil cuando necesitamos aplicar una misma operación a todos los elementos de un iterable y queremos obtener los 
resultados en un nuevo iterable sin usar bucles explícitos.'''