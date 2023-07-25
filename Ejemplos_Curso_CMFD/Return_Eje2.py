#múltiples retornos en funciones en Python.

## Parámetros por defecto:

'''Los parámetros por defecto permiten definir valores predeterminados para los argumentos de una función en caso de que no se proporcionen 
valores específicos al llamar a la función. 
Esto hace que los argumentos sean opcionales.'''

#Ejemplo de función con parámetros por defecto:


def saludar(nombre, saludo="Hola"):
    mensaje = f"{saludo}, {nombre}!"
    return mensaje

# Llamada a la función sin especificar el saludo
print(saludar("María"))
# Salida: "Hola, María!"

# Llamada a la función con un saludo personalizado
print(saludar("Carlos", "¡Hola amigo"))
# Salida: "¡Hola amigo, Carlos!

'''
En este ejemplo, la función saludar tiene un parámetro por defecto saludo="Hola". 
Si no se proporciona un valor para saludo, el valor predeterminado "Hola" será utilizado. 
Si se proporciona un valor específico para saludo, ese valor será utilizado en su lugar'''

'''Múltiples retornos:
Python permite que una función devuelva múltiples valores usando una tupla o cualquier otra estructura de datos para almacenar esos valores.'''

# Ejemplo de función con múltiples retornos:

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

# Llamada a la función y asignación de los valores de retorno a variables
resultado_suma, resultado_resta, resultado_mul, resultado_div = operaciones_basicas(20, 10)

print("Suma:", resultado_suma)               # Salida: Suma: 15
print("Resta:", resultado_resta)             # Salida: Resta: 5
print("Multiplicación:", resultado_mul)      # Salida: Multiplicación: 50
print("División:", resultado_div)            # Salida: División: 2.0

'''
En este ejemplo, la función operaciones_basicas(a, b) realiza algunas operaciones matemáticas con los valores de entrada a y b y 
devuelve los resultados de la suma, resta, multiplicación y división en una tupla. 
Luego, al llamar a la función, se almacenan esos valores de retorno en variables individuales.

Espero que estos ejemplos te ayuden a comprender cómo usar parámetros por defecto y múltiples retornos en funciones de Python. 
Estas características son muy útiles para hacer que tus funciones sean más flexibles y versátiles en diferentes situaciones.'''