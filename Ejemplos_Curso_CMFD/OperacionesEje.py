'''Los conjuntos (sets) en Python tienen varias operaciones útiles para realizar manipulaciones 
y comparaciones entre conjuntos. Aquí tienes algunas operaciones comunes que puedes realizar con conjuntos:

Unión de conjuntos (Union): 
La unión de dos conjuntos devuelve un nuevo conjunto que contiene todos los elementos de ambos conjuntos,
sin duplicados.'''

A = {1, 2, 3}
B = {3, 4, 5}

union = A.union(B)
print(union)  # Salida: {1, 2, 3, 4, 5}
'''En este ejemplo, se realiza la ONUAy Butilizando el método union(), 
y el resultado se almacena en el conjunto union. El conjunto resulta contiene todos los elementos de 
Ay B, sin duplicados.

Intersección de conjuntos (Intersection): 
La intersección de dos conjuntos devuelve un nuevo conjunto que contiene los elementos comunes a 
ambos conjuntos.'''

A = {1, 2, 3}
B = {3, 4, 5}

interseccion = A.intersection(B)
print(interseccion)  # Salida: {3}
'''esAy Butilizando el método intersection(), y el resultado se almacena en el conjunto `interseccion. 
El conjunto resultante contiene solo elA y B.'''

#Diferencia de conjuntos (Diferencia):
A = {1, 2, 3}
B = {3, 4, 5}

diferencia = A.difference(B)
print(diferencia)  # Salida: {1, 2}
'''En este ejemploAy Butilizando el método difference(), y el resultado se almacena en el conjunto 
diferencia. El conjunto resulta contiene los elementos '1' y '2' presenteA pero no en B.

Diferencia simétrica de conjuntos (Symmetric Difference): 
La diferencia simétrica entre dos conjuntos devuelve un nuevo conjunto que contiene los elementos 
que están en uno de los conjuntos'''

A = {1, 2, 3}
B = {3, 4, 5}

diferencia_simetrica = A.symmetric_difference(B)
print(diferencia_simetrica)  # Salida: {1, 2, 4, 5}
'''En este ejemplo, se calcula la diferencia simétrica entre los conjuntosAy Butilizando el método 
symmetric_difference(), y el resultado se almacena en el conjunto diferencia_simetrica. 
El conjunto resultante contiene los elementos '1', '2', '4' y '5

Estas son solo algunas de las operaciones que se pueden realizar con conjuntos en Python.
Los conjuntos también realizaron otras operaciones, como la comprobación de subconjuntos, 
superconjuntos, disyunción, entre otras. 
Puede consultar la documentación oficial de Python para obtener más información sobre las operaciones 
de conjunto: '''