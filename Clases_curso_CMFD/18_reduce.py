#en esta clase trabajaremos con reduce, se trata de uana función de python para reducir funciones, se trata de la transformacion de los elementos, reduciendo a un solo elemento
import functools #herramientas de python

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
resul = functools.reduce(lambda counter, item: counter + item, numbers)
print(numbers)
print(resul)

print('#' * 50)
#aca estamos creando la reduccion dentro de una funcion para tener el concepto mucho mas claro. La diferencia es que dontro de la funcion no emviamos la lambda 
def accum(counter, item):
  print('este es el cunter ==>> ', counter)
  print('este es el item ==>> ', item)
  return counter + item

resul = functools.reduce(accum, numbers)
print(resul) #con este codigo nos estara mostrando cada una de las interaciones, en las cuales estara sumando cada numero, uno con el otro hazta llegar en ese caso hazate el 20 
'''Reduce(fun, seq) tiene dos parametros:

Una función particular a aplicar a todos los elementos de una secuencia
Una secuencia de elementos.
Como funciona:

Primero toma los dos primeros elementos de la secuencia y aplica la función particular.
Toma el resultado anterior y a este valor mas el siguiente elemento de la secuencia le aplica la función particular.
El proceso continua hasta que no tiene mas elementos.
Retorna el resultado.'''