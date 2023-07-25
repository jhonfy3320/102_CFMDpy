'''
Para resolver el desafío, podemos utilizar una estructura condicional if-elif-else para evaluar el valor del artículo de tecnología 
recibido como entrada y retornar el mensaje correspondiente. '''

#Aquí está la función message_creator:

def message_creator(articulo):
    if articulo == "computadora":
        return "Con mi computadora puedo programar usando Python"
    elif articulo == "celular":
        return "En mi celular puedo aprender usando la app de Platzi"
    elif articulo == "cable":
        return "¡Hay un cable en mi bota!"
    else:
        return "Artículo no encontrado"

# Ejemplos de uso
print(message_creator("computadora"))  # Salida: "Con mi computadora puedo programar usando Python"
print(message_creator("celular"))      # Salida: "En mi celular puedo aprender usando la app de Platzi"
print(message_creator("cable"))        # Salida: "¡Hay un cable en mi bota!"
print(message_creator("audífonos"))    # Salida: "Artículo no encontrado"

'''
En esta función, evaluamos el valor de articulo utilizando if-elif-else. Si coincide con "computadora", "celular" o "cable", 
retornamos el mensaje correspondiente. Si no coincide con ninguna de estas opciones, retornamos el mensaje "Artículo no encontrado".

Ahora la función message_creator devuelve mensajes distintos según el artículo de tecnología recibido como entrada.'''


'''
test_computadora

test_celular

test_cable

test_default

¡Felicidades, todas las pruebas pasaron!'''