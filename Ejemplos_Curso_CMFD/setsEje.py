'''
Un conjunto (set) en Python es una colección desordenada de elementos únicos. 
Esto significa que un conjunto no permite tener elementos duplicados y no mantiene un orden específico de 
los elementos. Los conjuntos son objetos mutables, lo que significa que se pueden agregar, 
eliminar y modificar elementos.

Para crear un conjunto en Python, se utilizan llaves {}o la función set(). Por ejemplo:'''

frutas = {'manzana', 'naranja', 'plátano', 'papaya', 'aguacate'}

'''
En este caso, se crea un conjunto llamado frutas que contiene cinco elementos: 
'manzana', 'naranja' y 'plátano', 'papaya', 'aguacate'. Cada elemento en el conjunto es único y no se permite la duplicación.

Los conjuntos tienen varias operaciones útiles, como la unión, intersección, 
diferencia y comprobación de pertenencia. Aquí hay algunos ejemplos reales para ilustrar su uso:

Eliminación de elementos duplicados:
'''
numeros = [1, 2, 3, 4, 2, 3, 5, 1, 9, 3, 5, 6, 8, 9, 11, 10] 
numeros_unicos = set(numeros)
print(numeros_unicos)  # Salida: {1, 2, 3, 4, 5}


'''En este ejemplo, se tiene una lista de números numerosque contiene elementos duplicados. 
Al convertir la lista en un conjunto utilizando set(numeros). 
se eliminan los elementos duplicados y se obtiene un conjunto numeros_unicoscon elementos únicos.

Operaciones de conjunto:'''

frutas1 = {'manzana', 'naranja', 'plátano'}
frutas2 = {'pera', 'manzana', 'durazno'}

# Unión de conjuntos
frutas_union = frutas1 | frutas2
print(frutas_union)  # Salida: {'manzana', 'naranja', 'plátano', 'pera', 'durazno'}

# Intersección de conjuntos
frutas_interseccion = frutas1 & frutas2
print(frutas_interseccion)  # Salida: {'manzana'}

# Diferencia de conjuntos
frutas_diferencia = frutas1 - frutas2
print(frutas_diferencia)  # Salida: {'naranja', 'plátano'}

'''
En este ejemplo, se tienen dos conjuntos frutas1y frutas2. 
Se realizan operaciones de conjuntos utilizando los operadores |(unión), &(intersección) y -(diferencia) 
para obtener la unión, intersección y diferencia de los conjuntos.

Los conjuntos son útiles cuando se necesita almacenar elementos únicos y realizar operaciones de conjuntos 
eficientes, como búsqueda de elementos únicos, combinación de conjuntos y eliminación de duplicados. 
Son especialmente útiles en situaciones donde el orden de los elementos no es importante y la eficiencia 
en la búsqueda es crucial.'''