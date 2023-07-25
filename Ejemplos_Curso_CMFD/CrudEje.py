'''Los conjuntos (sets) en Python son objetos mutables, lo que significa que se pueden modificar agregando, eliminando o actualizando elementos. 
Aquí tienes algunas operaciones comunes para modificar conjuntos:

Agregar elementos a un conjunto:
Utilizando el método add(): Agrega un único elemento al conjunto.
Utilizando el método update(): Agrega múltiples elementos al conjunto.'''

frutas = {'manzana', 'naranja', 'plátano'}

frutas.add('pera')
print(frutas)  # Salida: {'manzana', 'naranja', 'plátano', 'pera'}

frutas.update(['mango', 'uva'])
print(frutas)  # Salida: {'manzana', 'naranja', 'plátano', 'pera', 'mango', 'uva'}
#En este ejemplo, se agrega un elemento individual ('pera') al conjunto utilizando el método add(). Luego, utilizando el método update(), se agregan varios elementos ('mango' y 'uva') al conjunto mediante una lista.

'''Eliminar elementos de un conjunto:
Utilizando el método remove(): Elimina un elemento específico del conjunto. Si el elemento no existe, se produce un error.
Utilizando el método discard(): Elimina un elemento específico del conjunto. Si el elemento no existe, no se produce un error.
Utilizando el método pop(): Elimina y devuelve un elemento arbitrario del conjunto.'''

frutas = {'manzana', 'naranja', 'plátano'}

frutas.remove('naranja')
print(frutas)  # Salida: {'manzana', 'plátano'}

frutas.discard('pera')
print(frutas)  # Salida: {'manzana', 'plátano'}

elemento_eliminado = frutas.pop()
print(frutas)  # Salida: {'plátano'}
print(elemento_eliminado)  # Salida: 'manzana'
'''En este ejemplo, se eliminan elementos específicos del conjunto utilizando los métodos remove() y discard(). 
El método pop() se utiliza para eliminar y devolver un elemento arbitrario del conjunto.'''

'''Actualizar elementos de un conjunto:
Utilizando el método update(): Reemplaza los elementos del conjunto con elementos de otro iterable.'''
frutas = {'manzana', 'naranja', 'plátano'}
nuevas_frutas = ['mango', 'uva']

frutas.update(nuevas_frutas)
print(frutas)  # Salida: {'manzana', 'naranja', 'plátano', 'mango', 'uva'}
'''En este ejemplo, se actualiza el conjunto frutas agregando los elementos de la lista nuevas_frutas utilizando el método update(). 
Los elementos existentes se mantienen y se agregan los nuevos elementos.

Recuerda que los conjuntos son colecciones desordenadas, por lo que no hay garantía sobre el orden de los elementos en un conjunto. 
Además, los conjuntos no permiten elementos duplicados, por lo que si se agrega un elemento que ya existe, 
no se producirán cambios en el conjunto.'''