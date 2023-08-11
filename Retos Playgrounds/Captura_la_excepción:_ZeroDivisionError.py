'''
Para capturar la excepción ZeroDivisionError en la función my_divide, debemos utilizar un bloque try-except que maneje la división 
y capture la excepción en caso de que el segundo argumento sea igual a 0.
'''
## Aquí está la implementación de la función my_divide con el manejo de la excepción:

def my_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        return "No se puede dividir por 0"

response = my_divide(10, 2)
print(response)  # Output: 5

response = my_divide(10, 0)
print(response)  # Output: No se puede dividir por 0
'''
Cuando el segundo argumento es 0, la división generará una ZeroDivisionError y se capturará en el bloque except, 
lo que nos permitirá retornar el mensaje "No se puede dividir por 0" en lugar de dejar que la excepción detenga el programa.'''