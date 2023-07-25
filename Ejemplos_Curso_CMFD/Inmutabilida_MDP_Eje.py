'''
Para mantener la inmutabilidad de los datos al usar map(), podemos utilizar la función functools.partial() junto con map(). 
La función functools.partial() permite aplicar una función con algunos argumentos predefinidos y luego usar map() para aplicar esa función 
parcial a los elementos de un iterable.'''

## Veamos un ejemplo para entender cómo mantener la inmutabilidad con map() y functools.partial():

from functools import partial

def sumar(numero, cantidad):
    return numero + cantidad

numeros = [1, 2, 3, 4, 5]

# Utilizando functools.partial() para aplicar sumar con el argumento cantidad=2
sumar_dos = partial(sumar, cantidad=2)

# Usando map() con la función parcial sumar_dos
nuevos_numeros = list(map(sumar_dos, numeros))

print(numeros)        # Salida: [1, 2, 3, 4, 5]
print(nuevos_numeros)  # Salida: [3, 4, 5, 6, 7]

'''En este ejemplo, definimos una función sumar() que toma dos argumentos, numero y cantidad, y devuelve la suma de ambos. 
Luego, creamos una función parcial sumar_dos utilizando functools.partial() para aplicar sumar() con el argumento cantidad=2.

Finalmente, utilizamos map() para aplicar la función parcial sumar_dos a cada elemento de la lista numeros. 
Esto nos permite obtener un nuevo iterable nuevos_numeros con los resultados de la suma sin modificar la lista original numeros.

De esta manera, podemos utilizar map() junto con functools.
partial() para aplicar funciones con argumentos predefinidos a los elementos de un iterable y mantener la inmutabilidad de los datos originales.'''