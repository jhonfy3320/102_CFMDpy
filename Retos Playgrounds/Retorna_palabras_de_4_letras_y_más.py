'''
Para resolver el desafío, utilizaremos la función filter() junto con una función lambda para filtrar la lista de palabras y mantener 
solo aquellas que tengan 4 o más letras.'''

def filter_by_length(words):
    # Utilizamos filter() para filtrar las palabras usando una función lambda
    # La función lambda devuelve True si la longitud de la palabra es 4 o más
    result = list(filter(lambda word: len(word) >= 4, words))
    return result

# Ejemplo de uso
lista_palabras = ["casa", "perro", "árbol", "gato", "sol", "flor", "mesa"]
resultado_filtrado = filter_by_length(lista_palabras)
print(resultado_filtrado)  # Salida: ['casa', 'perro', 'árbol', 'flor', 'mesa']

'''
En este ejemplo, definimos la función filter_by_length() que toma una lista words como argumento. 
Utilizamos filter() junto con la función lambda lambda word: len(word) >= 4 para filtrar las palabras de la lista. 
La función lambda evalúa si la longitud de cada palabra es mayor o igual a 4 y retorna True si se cumple la condición.

La expresión filter(lambda word: len(word) >= 4, words) crea un objeto filter con las palabras que cumplen con la condición. 
Finalmente, convertimos este objeto filter a una lista usando list() para obtener la lista result con las palabras filtradas.

Al llamar a filter_by_length() con la lista de palabras lista_palabras, obtenemos la lista filtrada que contiene solo las palabras 
con 4 o más letras. En este caso, la lista resultante sería ['casa', 'perro', 'árbol', 'flor', 'mesa'].

La función filter() es una herramienta útil para filtrar elementos de una lista o cualquier otro iterable basándose en una condición, 
lo que nos permite seleccionar solo los elementos que cumplan con cierta condición específica. 
En este caso, hemos filtrado la lista de palabras manteniendo solo aquellas con 4 o más letras.'''