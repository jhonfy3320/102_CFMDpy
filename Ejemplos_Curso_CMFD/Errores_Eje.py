'''
En Python, los errores se conocen como excepciones y ocurren cuando hay algún problema en la ejecución del código. 
Estas excepciones pueden ser de diferentes tipos, dependiendo de la naturaleza del error. 
Algunos ejemplos comunes de errores en Python incluyen:'''

## SyntaxError: 
'''
Este error ocurre cuando hay un error de sintaxis en el código. 
Por ejemplo, si olvidamos cerrar una comilla o paréntesis, Python generará un SyntaxError.
Ejemplo de SyntaxError:'''
# Error de sintaxis, falta cerrar la comilla
#print("Hola)
      
## NameError: 
'''
Este error ocurre cuando intentamos acceder a una variable o función que no está definida.
Ejemplo de NameError:'''

# La variable "x" no está definida
# print(x)

## TypeError: 
'''
Este error ocurre cuando se realiza una operación entre objetos de tipos incompatibles.
Ejemplo de TypeError:
'''
# Intentando sumar un entero con una cadena
x = 5 + "Hola"

## IndexError: 
'''
Este error ocurre cuando intentamos acceder a un índice que está fuera del rango de una lista o secuencia.
Ejemplo de IndexError:'''

# Intentando acceder al índice 5 de una lista con 3 elementos
lista = [1, 2, 3]
print(lista[5])

## KeyError: 
'''
Este error ocurre cuando intentamos acceder a una clave que no existe en un diccionario.
Ejemplo de KeyError:'''
# Intentando acceder a una clave inexistente en el diccionario
diccionario = {"nombre": "Juan", "edad": 25}
print(diccionario["apellido"])

'''
ZeroDivisionError: 
Este error ocurre cuando intentamos dividir entre cero.
Ejemplo de ZeroDivisionError:'''

# Intentando dividir entre cero
resultado = 10 / 0
'''
Para manejar los errores y evitar que el programa se detenga, podemos utilizar bloques try-except. 
De esta manera, podemos capturar la excepción y realizar una acción específica en caso de que ocurra un error.'''

# Ejemplo de manejo de excepciones con try-except:

try:
    x = 5 + "Hola"
except TypeError as e:
    print("Se produjo un error de tipo:", e)
'''
En este ejemplo, al intentar sumar un entero con una cadena, se generará un TypeError. 
Sin embargo, el bloque try-except permite capturar este error y mostrar un mensaje personalizado en lugar de detener la ejecución del programa.'''

'''
Es importante manejar adecuadamente las excepciones en Python para que nuestro código sea más robusto y 
pueda manejar situaciones inesperadas de manera adecuada. Siempre es recomendable utilizar bloques try-except 
para prevenir que el programa se bloquee en caso de errores.
'''



