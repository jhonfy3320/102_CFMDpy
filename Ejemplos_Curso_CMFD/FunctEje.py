'''Las funciones en Python son bloques de código reutilizables que pueden realizar tareas específicas y devolver resultados. 
Son una parte fundamental de la programación, ya que te permiten dividir el código en piezas más pequeñas y manejables, 
lo que facilita la organización y el mantenimiento del programa. 
Las funciones se definen utilizando la palabra clave def, seguida del nombre de la función, 
paréntesis que pueden contener parámetros de entrada (opcional) y dos puntos :. 
El código de la función está indentado y se ejecuta cuando la función es llamada.'''

## Sintaxis básica de una función en Python:

def nombre_de_funcion(parametro1, parametro2):
    # Código de la función
    # Puede contener instrucciones, cálculos, operaciones, etc.
    return nombre_de_funcion # Opcional: devuelve un valor (resultado) si es necesario

## Aquí tienes un ejemplo sencillo de una función que suma dos números y devuelve el resultado:

def suma(a, b):
    resultado = a + b
    return resultado

# Llamada a la función y almacenamiento del resultado en la variable "total"
total = suma(5, 3)
print(total)  # Salida: 8

'''En este ejemplo, definimos una función llamada suma que toma dos parámetros a y b, realiza la operación de suma y devuelve el resultado. 
Luego, llamamos a la función pasando los valores 5 y 3, y almacenamos el resultado de la suma en la variable total, que luego se imprime.

Las funciones pueden tener cero o más parámetros de entrada, y pueden o no devolver un valor utilizando la declaración return. 
También pueden realizar cualquier tipo de operación, cálculo o lógica necesaria para completar su tarea.

Las funciones son herramientas poderosas para dividir tareas complejas en partes más pequeñas y manejables, 
lo que hace que el código sea más legible, reutilizable y fácil de mantener.'''