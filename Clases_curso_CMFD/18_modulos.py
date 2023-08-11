#¿Qué son los modulos en Python ejemplos?
#Los módulos en Python son simplemente archivos Python con la extensión . 
#.py, que implementa un conjunto de funciones. Los módulos son importados desde otros módulos usando el comando import . Para importar un módulo, usamos el comando import 
import sys
print(sys.path)#con el  modulo sys podemos saber en donde se encuentra hubicado el edictor en el que me encuentro trabajando 

import re #espreciones regulares 
tex = 'mi nuemero de telefono es 3217181593, codigo pais +57, numero de la suerte 1133'#con re podemos encontar de esta cadena de string todo lo que sean numeros 
resul = re.findall('[0-9]+', tex)
print(resul)
#NOTA ==>> las espreciones regulares tienen su propia simtasys 

import time #manejo de horas y fechas 
timestamp = time.time()
print(timestamp)#aca nos dara una fecha que es de la computadora es muy compleja de entender 

timestamp = time.time()
local = time.localtime() # este es un formato iunix mas para computadores 
result = time.asctime(local)
print(result)# este es un formato para que lo entiendan los humanos 

import collections # utilidada para menejar listas en Python 
numbers = [1,1,1,1,1,2,2,3,4,5,6,6,7,8,8,8,9,0,0,7,7,6,1,2,3,4,5,6,7,8,9,0,1,2,3,4]
counter = collections.Counter(numbers)
print(numbers)
print(counter) # con este modulo podemos encontra la frecuencia en la que se encuetra cierto elemento de nuetra lista ded numeros 

# en esta clase tubimos el primer hacercamiento a los modulos, debemos profundizar mucho mas en ello