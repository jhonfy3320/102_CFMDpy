'''
reto utilizando map() con precios de productos de supermercado. 
Supongamos que tenemos una lista de precios de algunos productos y queremos aplicar un descuento del 10% a cada precio. 
Para mantener la inmutabilidad, utilizaremos map() para aplicar una función a cada precio y obtener los precios con el descuento en una nueva 
lista sin modificar la original.'''

def aplicar_descuento(precio):
    return precio * 0.9  # Descuento del 10%

# Lista de precios de productos
precios_originales = [100, 200, 300, 400, 500]

# Usando map() para aplicar el descuento a cada precio
precios_descuento = list(map(aplicar_descuento, precios_originales))

# Mostrar los precios originales y los precios con descuento
print("Precios originales:", precios_originales)
print("Precios con descuento:", precios_descuento)

'''
En este ejemplo, definimos una función aplicar_descuento() que toma un precio como argumento y devuelve el precio con el descuento del 10%. 
Luego, tenemos una lista precios_originales con algunos precios de productos.

Utilizamos map(aplicar_descuento, precios_originales) para aplicar la función aplicar_descuento() a cada precio de la lista precios_originales. 
El resultado es un objeto map, por lo que lo convertimos a una lista usando list() para obtener los precios con descuento en la lista precios_descuento.

Al imprimir los precios originales y los precios con descuento, podemos ver que la lista precios_originales permanece inmutable, 
mientras que la lista precios_descuento contiene los precios con el descuento aplicado. 
De esta manera, hemos logrado aplicar el descuento sin modificar la lista original.'''