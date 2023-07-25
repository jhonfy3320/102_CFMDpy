'''En Python, la instrucción return se utiliza dentro de una función para devolver un valor como resultado de la ejecución de la función. 
Cuando una función alcanza la declaración return, termina su ejecución y devuelve el valor especificado. 
El valor devuelto por la función puede ser de cualquier tipo de datos válido en Python, como enteros, cadenas, listas, diccionarios, etc.'''

## Sintaxis de return:

def nombre_de_funcion(parametro1, parametro2):
    # Código de la función
    # Puede contener instrucciones, cálculos, operaciones, etc.
    return #valor_a_devolver

#Ejemplo:

def suma(a, b):
    resultado = a + b
    return resultado

total = suma(5, 3)
print(total)  # Salida: 8
'''
En este ejemplo, la función suma(a, b) toma dos parámetros a y b, realiza la suma y devuelve el resultado utilizando return resultado. 
El valor de resultado (en este caso, 8) se devuelve cuando se llama a la función suma(5, 3) y se almacena en la variable total.

Es importante tener en cuenta que una función puede tener múltiples declaraciones return en diferentes puntos del código. 
Sin embargo, una vez que una declaración return se ejecuta, la función finaliza y no se ejecutan más líneas de código dentro de ella. 
Esto significa que cualquier código que esté después de una declaración return no se ejecutará.'''

# Por ejemplo:

def multiplicacion(a, b):
    resultado = a * b
    if resultado > 10:
        return "El resultado es mayor que 10"
    else:
        return resultado
    print("Esto no se imprimirá")

resultado1 = multiplicacion(3, 5)
resultado2 = multiplicacion(4, 3)
print(resultado1)  # Salida: 15
print(resultado2)  # Salida: "El resultado es mayor que 10"

'''
En este ejemplo, la función multiplicacion(a, b) toma dos parámetros, realiza la multiplicación y luego utiliza una declaración if 
para verificar si el resultado es mayor que 10. Dependiendo del resultado, la función devuelve un valor diferente. 
Si el resultado es mayor que 10, se devuelve la cadena "El resultado es mayor que 10". 
Si el resultado es menor o igual a 10, se devuelve el resultado de la multiplicación. 
La línea print("Esto no se imprimirá") después de la declaración return nunca se ejecutará.'''