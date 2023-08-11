'''
El manejo de excepciones en Python es una técnica utilizada para controlar y responder adecuadamente a los errores que pueden ocurrir 
durante la ejecución de un programa. 
Cuando ocurre una excepción, el flujo normal del programa se interrumpe y Python busca un bloque except 
que coincida con el tipo de excepción que se ha generado. 
Si encuentra un bloque except que coincida, ejecutará el código dentro de ese bloque para manejar la excepción de manera adecuada.'''

'''
El manejo de excepciones se realiza utilizando la estructura try-except. 
El bloque try contiene el código que podría generar una excepción, y el bloque except contiene el código para manejar esa excepción.'''

## Sintaxis básica del manejo de excepciones:

#try:
    # Código que podría generar una excepción
    # ...
#except TipoDeExcepcion as nombreDeExcepcion:
    # Código para manejar la excepción
    # ...
# El bloque except puede tener diferentes formas para manejar diferentes tipos de excepciones. Por ejemplo:

## Manejo de una excepción específica:

try:
    x = 5 / 0
except ZeroDivisionError as e:
    print("Error: No se puede dividir entre cero.")

## Manejo de varias excepciones:

try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError as e:
    print("Error: El índice está fuera del rango de la lista.")
except ZeroDivisionError as e:
    print("Error: No se puede dividir entre cero.")

## Manejo de cualquier excepción:

'''
try:
    # Código que podría generar una excepción
    # ...
except Exception as e:
    print("Error:", e)'''


'''
Es importante tener en cuenta que el manejo de excepciones no debe usarse para ocultar errores o problemas en el código. 
Es una herramienta para lidiar con situaciones inesperadas y permitir que el programa siga funcionando a pesar de los errores. 
Además, es posible tener bloques try-except anidados para manejar excepciones específicas en diferentes niveles del código.'''

# También se puede incluir un bloque else después de los bloques except, que se ejecutará si no se produce ninguna excepción en el bloque try.

'''
try:
    # Código que podría generar una excepción
    # ...
except Exception as e:
    print("Error:", e)
else:
    print("El código se ejecutó correctamente.")
'''

'''
El manejo de excepciones es una práctica importante en la programación para crear programas más robustos y tolerantes a errores, 
lo que mejora la experiencia del usuario y facilita la depuración y el mantenimiento del código.'''




