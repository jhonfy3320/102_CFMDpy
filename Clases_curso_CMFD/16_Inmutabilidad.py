producto = [
  {
    'procucto': 'compresor a/c',
    'precio': 1500000
  },
  {
    'producto': 'condensador',
    'precio': 450000
  },
  {
    'producto': 'evaporador',
    'precio': 520000
  },
  {
    'producto': 'ventiladores',
    'precio': 380000
  }
]
def add_impuestos(producto):
  new_producto = producto.copy()
  producto['impuestos'] = producto['precio'] * .19
  return new_producto#aca estamos imutando la lista, para que en este caso no nos salga los impuestos(palabra)

new_producto = list(map(add_impuestos, producto))
print('nueva lista')
print(new_producto)
print('#' * 50)
print('anterior lista ')
print(producto)
#como podemos notar en el codigo y al ejecutarlo, estamos imutando las listas para que no se vean modificadas 

print('*' * 60)

'''Map con inmutabilidad
El problema de la modificacion de la lista original tras aplicar una transformacion con un map se debe a la referencia en memoria, es decir, cuando trabajamos con un diccionarios hay un espacio en memoria reservada para ese diccionario; al aplicar una transformacion sobre el diccionario, los nuevos valores se asignan al diccionario como una referencia en memoria; entonces al hacer una modificacion se aplica tanto para el array original como para el nuevo ya que ambos comparten la misma referencia en memoria.

Solucion con el metodo copy()'''

#-------------Quitar la referencia en memoria del diccionario------------------
items = [
  {
    'product':'camisa',
    'price':100
  },
  {
    'product':'pantalon',
    'price':300
  },
  {
    'product':'vestido',
    'price':150
  },
  {
    'product':'chaqueta',
    'price':400
  }
]

# al agregar el metodo copy desreferenciamos el array original con el nuevo
def add_taxes(items):
  new_item = items.copy()
  new_item['taxes'] = new_item['price'] * .19
  return new_item
  
new_items = list(map(add_taxes, items))
print('New list')
print(new_items)

[{'product': 'camisa', 'price': 100, 'taxes': 19.0}, 
{'product': 'pantalon', 'price': 300, 'taxes': 57.0}, 
{'product': 'vestido', 'price': 150, 'taxes': 28.5}, 
{'product': 'chaqueta', 'price': 400, 'taxes': 76.0}]

print('Old list')
print(items)

[{'product': 'camisa', 'price': 100}, 
{'product': 'pantalon', 'price': 300}, 
{'product': 'vestido', 'price': 150}, 
{'product': 'chaqueta', 'price': 400}]