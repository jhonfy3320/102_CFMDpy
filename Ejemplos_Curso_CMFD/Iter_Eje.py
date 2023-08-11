'''
Claro, para dar ejemplos de iterables con diferentes marcas y cilindros de automóviles, 
podemos utilizar listas de diccionarios donde cada diccionario represente un automóvil con la marca y el cilindro como atributos. 
Luego, podemos iterar sobre la lista para encontrar los automóviles más costosos y de mayor cilindraje. '''

## Aquí tienes un ejemplo:


# Ejemplo de lista de diccionarios con marcas y cilindrajes de automóviles
autos = [
    {"marca": "Toyota", "cilindraje": 2000, "precio": 25000},
    {"marca": "Honda", "cilindraje": 1800, "precio": 28000},
    {"marca": "BMW", "cilindraje": 3000, "precio": 50000},
    {"marca": "Ford", "cilindraje": 2500, "precio": 22000},
    {"marca": "Chevrolet", "cilindraje": 1800, "precio": 20000},
    {"marca": "Audi", "cilindraje": 3500, "precio": 60000}
]

# Encontrar los autos más costosos y de mayor cilindraje
max_precio = max(autos, key=lambda auto: auto["precio"])
max_cilindraje = max(autos, key=lambda auto: auto["cilindraje"])

print("Automóvil más costoso:")
print(max_precio)

print("\nAutomóvil de mayor cilindraje:")
print(max_cilindraje)

'''
En este ejemplo, hemos utilizado la función maxjunto con unamaxtoma un iterable (en este caso, la lista de automóviles) 
y devuelve el elemento con el valor má'''