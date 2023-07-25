'''
Para filtrar listas en Python, puedes utilizar la función filter(), que es otra higher-order function similar a map(). 
La función filter() se utiliza para filtrar elementos de un iterable (como una lista) basándose en una función de condición 
(también llamada función predicado). 
La función de condición debe retornar True o False para cada elemento del iterable, y solo los elementos para los cuales la función de 
condición retorna True se mantendrán en el resultado.'''

#filter este biene por defecto en las funcionalidades de python y nos sirve para filtrar listas, filtra aquellos elementos que no cumplen con ciertas carateristicas, los seleciona y crea una nueva lsitas con esos elementos 
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(numbers)
print(new_numbers)
#aca estamos viendo la sintaxys basica de un filtro 

def es_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando filter() para filtrar los números pares
numeros_pares = list(filter(es_par, numeros))

print(numeros_pares)  # Salida: [2, 4, 6, 8, 10]

'''
En este ejemplo, definimos la función es_par() que toma un número como argumento y devuelve True si el número es par, o False en caso contrario.

Luego, tenemos una lista numeros que contiene algunos números. Utilizamos filter(es_par, numeros) para aplicar la función es_par() 
a cada número de la lista. 
Solo los números para los cuales la función es_par() retorna True (es decir, los números pares) se mantienen en el resultado.

Finalmente, convertimos el objeto filter a una lista usando list() para obtener la lista numeros_pares con los números filtrados.

Es importante mencionar que, al igual que map(), filter() también retorna un objeto filter en Python 3.x, por lo que debemos convertirlo 
a una lista para obtener los resultados reales. En Python 2.x, filter() retorna una lista directamente.

filter() es una herramienta poderosa para filtrar elementos de una lista o cualquier otro iterable, y puede ser útil cuando 
necesitas seleccionar solo ciertos elementos que cumplan con cierta condición.'''