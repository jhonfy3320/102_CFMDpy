'''¿Que es lambda?
Son conocidas como Funciones Anónimas o lambdas, en donde no tienen un identificador o no tienen un nombre, se puede definir su estructura de la siguiente manera: lambda argumentos: expresión, las funciones lambda pueden tener los argumentos que se requieran pero solo una linea de código o una expresión.

Sintaxis
lambda arguments : expression

Queremos incrementar el valor de una serie según la cantidad que le hayamos dado para ello tenemos el siguiente ejemplo:'''
#trabajando con la funcion 
def incremet(x):
  return x + 1
result = incremet(10)
print(40) 
#transformando la funcion anterior en una landas
def incremet(x):
  return x + 1
lambda x : x + 1
result = incremet(10)
print(40) 
#creando una version dos del la funcion con landa 
def incremet(x):
  return x + 60
incremet_2 = lambda x : x + 60
result = incremet_2(40)
print(result) 
#dos funciones que hacen lo mismo pero con un lambda incluida 

#====>>> creando un lambda que resive dos valores 
full_name = lambda name, last_name: f'full_name is {name.title()}{last_name.title()}'

test = full_name('nicolas y emanuel primos ', 'ocoro osorio')
print(test)
#aca miramos las lambda funcion que es crearlas dentro de una funcion 