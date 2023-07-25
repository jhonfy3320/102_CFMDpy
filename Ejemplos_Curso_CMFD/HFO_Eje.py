'''Es importante aclarar que una función dentro de otra función no califica como una higher-order function 
(función de orden superior) en Python.

Una higher-order function es aquella que toma una o más funciones como argumentos y/o devuelve una función como resultado. L
a característica clave de una higher-order function es que opera con funciones como si fueran objetos, lo que permite una mayor flexibilidad 
y modularidad en el código.'''

## Veamos un ejemplo correcto de higher-order function en Python:

def operacion_matematica(funcion, a, b):
    return funcion(a, b)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

resultado_suma = operacion_matematica(suma, 5, 3)
print(resultado_suma)  # Salida: 8

resultado_resta = operacion_matematica(resta, 10, 4)
print(resultado_resta)  # Salida: 6

resultado_multiplicacion = operacion_matematica(multiplicacion, 2, 5)
print(resultado_multiplicacion)  # Salida: 10


'''En este ejemplo, la función operacion_matematica es una higher-order function que toma una función (funcion) y dos valores (a y b) como argumentos. 
Luego, aplica la función dada a los valores a y b, y devuelve el resultado.

Las funciones suma, resta y multiplicacion son funciones simples que realizan operaciones matemáticas específicas. 
Al llamar a operacion_matematica(suma, 5, 3), estamos pasando la función suma como argumento a operacion_matematica, 
lo que nos permite realizar una suma de los números 5 y 3.

En resumen, una higher-order function es aquella que trabaja con funciones como si fueran objetos, permitiendo una mayor flexibilidad y 
reutilización del código al recibir funciones específicas como argumentos o devolver funciones como resultado.'''