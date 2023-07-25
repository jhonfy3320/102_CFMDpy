'''
La función reduce() en Python se encuentra en el módulo functools y se utiliza para aplicar una función binaria 
(que toma dos argumentos) de forma acumulativa a los elementos de un iterable, de izquierda a derecha, para reducirlos a un solo valor.'''

#La función reduce() toma dos argumentos: 
#la función binaria que se aplicará de forma acumulativa y el iterable que se desea reducir. 
#La función binaria debe tomar dos argumentos y devolver el resultado de la operación. 
#El resultado de la primera operación se toma como primer argumento para la segunda operación, y así sucesivamente, hasta que se haya aplicado la 
#función a todos los elementos del iterable.

'''Para utilizar reduce(), primero debes importarla del módulo functools. 
A continuación, te mostraré un ejemplo de cómo usar reduce() para calcular el producto de todos los elementos de una lista:'''


from functools import reduce

def producto(x, y):
    return x * y

numeros = [1, 2, 3, 4, 5]

# Usando reduce() para calcular el producto de todos los elementos de la lista
resultado = reduce(producto, numeros)

print(resultado)  # Salida: 120 (1 * 2 * 3 * 4 * 5)
'''
En este ejemplo, hemos definido la función producto(x, y) que toma dos argumentos x e y y devuelve el producto de ambos. 
Luego, tenemos una lista numeros con algunos valores.

Utilizamos reduce(producto, numeros) para aplicar la función producto() acumulativamente a todos los elementos de la lista. 
En la primera iteración, x será 1 y y será 2, por lo que se calculará el producto de 1 * 2 = 2. En la siguiente iteración, x será 2 
(resultado de la iteración anterior) y y será 3, por lo que se calculará el producto de 2 * 3 = 6. 
Y así sucesivamente hasta que se haya aplicado la función a todos los elementos de la lista.

El resultado final es 120, que es el producto de todos los elementos de la lista [1, 2, 3, 4, 5].

La función reduce() es útil cuando se desea aplicar una operación acumulativa a los elementos de un iterable para reducirlos a un solo valor, 
como el producto, la suma, el máximo o el mínimo, entre otros. 
Es importante tener en cuenta que en Python 3, reduce() se ha movido al módulo functools y ya no es una función incorporada en Python 3.x.'''