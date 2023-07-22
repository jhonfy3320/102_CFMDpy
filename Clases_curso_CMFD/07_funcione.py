#en este segundo mudulo empezaremos a trabajar con funciones, para cuando tenemos grandes 
#bloques de codigo que se repiten muchas veces, para evitar la repeticion usaremos las finciones, 
#reutilizando ese codigo en diferentes puntos del programa o proyecto

'''funcion def'''

print('hola estoy aprendien python')

def my_print():
  print('esta es una funcion, para repetir bloues codigo')
  print('nico y emanuel tambien quieren aprender a programar')
  print('esta es una funcion, para repetir bloues codigo')
  print('nico y emanuel tambien quieren aprender a programar')
  #dentro de la funcion esta definido su comportamiento, que es este bloque de codigo, se ejecutara todod lo que esta dentro dela funcion 
my_print()
print('#' * 50)

def my_print(text):
  print(text * 4)#aca tenemos el parametro definido , que sera el comportamiento de la funcion, segun lo que queremo que imprima y las veces que lo imprima 

my_print('esta es una funcion, para repetir bloues codigo')
my_print('emanuel, nico')
#aca estamos repitiendo codigo 

print('#' * 50)
#funciones con operadores aritmeticos 
a = 40
b = 20
c = a * b
print(c)

def suma(a, b):
  print(a + b)
suma(20, 40)
suma(100, 90)

print('#' * 50)
#una funcion dentro de otra funcion
def suma(a, b):
  my_print(a * b)
suma(20, 40)
suma(100, 90)

print('Hola, Platzinauta') 
#Agregando una funcion print

def greeting(text):
# Aquí estamos agregando una funcion y su sintaxis.
# Junto con sus parametros en este caso 'text'
  print('This is my print')
  print('This is my print 2')
  print(text)

greeting('parametro')
#  Una manera de llamar a la función
greeting('Texto ejemplo, llamando a la función desde su parametro. ' * 2)
#Aquí otro ejemplo con suma
def suma(a,b):
  print(a + b)
#  Imprimimos el resultado a consola
suma(200, 100) 
# llamamos a la función con parametros