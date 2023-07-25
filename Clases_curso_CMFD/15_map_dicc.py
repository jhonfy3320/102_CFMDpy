# trabajando con map cambiando el tipo de dato, ya sean enteros, decimales o cadena de caracteres

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
precio = list(map(lambda item: item['precio'], producto))
print(precio)#aca estamos sacando un diccionario con los precios de cada atributo
print(producto)
print('#' * 50)
#agregando impuestos a nuestros productos  en los diccionarios  diccionarios 
def add_impuestos(producto):
  producto['impuestos'] = producto['precio'] * .19
  return producto

new_producto = list(map(add_impuestos, producto))
print(new_producto)
print(producto)#===>> en esta clase se Aprende a trabajar con map en los diccionarios, aunque debemos de tener un poco de cuidado, ya que al modificar un atributo de un diccionario puede estar modificando todo el array original, y generando un nuevo problema

print('#*'* 50)
producto =[
    {'product': 'shirt',
    'price':120
    },
    {'product': 'pants',
    'price':160
    },
    {'product': 'jacket',
    'price':205
    }
]

new_items = list(map( lambda x: x|{'tax': x['price']*0.19} ,producto)) 

print(new_items)   
print(producto)
