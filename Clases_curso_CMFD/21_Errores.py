# print(0 / 0)
# print(result)
print('Hola')

suma = lambda x,y: x + y
assert suma(2,2) == 4

print('Hola 2')

age = 10
if age < 18:
  raise Exception('No se permiten menores de edad')

print('Hola 2')

'''
Prueba de Python excepto

Una buena noticia es que Python tiene un buen número de excepciones integradas para detectar errores en nuestro código. 
Además, nos brinda la oportunidad de crear excepciones personalizadas cuando ninguna de las excepciones integradas se adapta a 
nuestras necesidades.
¿Qué es una excepción?

Entonces, ¿qué es una excepción en Python? Bueno, en términos simples, cada vez que el intérprete de 
Python intenta ejecutar un código no válido, genera una excepción y, en los casos en que dicha excepción no se maneja, 
interrumpe el flujo normal de las instrucciones del programa e imprime un rastreo.'''