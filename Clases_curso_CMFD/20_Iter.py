'''ITERABLES
Un iterable se define como el objeto que contiene un número contable con valores y este al tener un valor puede recorrer uno a 
uno los elementos que la contienen como una estructura de datos y operar con ellos, pero a la vez se rigen bajo la instrucción 
que se le es dada, con lo cual son dependientes de la instrucción a recibir.

Los metodos de su uso son dos __iter__() y __next__() .

Veamos un ejemplo:

Tenemos una serie de frutas las cuales debemos recorrer una a una para saber cuales son las que están dentro de la lista'''


for i in range(0, 1001):
  print(i) # iteracion de de un rango de numero a cierta cantidad 

my_iter = range(0, 21)
print(my_iter) # aca solo nos imprimira el rango que queremos que nos itere, como no esta dentro de un for no se iterarar el rango 

my_iter = iter(range(0, 21))
print(my_iter)#este es uniterador sin el for, solo que es manual
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))#para podelo iterar debemos ingresarle un (next), y se iterara uno a uno manuelamente, cada next se octine un valor de la iteracion hazta llegar al rango que le asignamos 

#NOTA al hacer la iteracion manuela llegara el momento del limite de esa iteracion , lo que se mecionava anteriormente con respecto al rango, al llegar a ese limite me arrojara el error de iteraciones 