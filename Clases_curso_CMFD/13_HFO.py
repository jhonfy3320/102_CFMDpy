#===>> HFO funciones de orden superior. esto lo que nos quiere decir es que yo puedo emviar una funcion y ejeucutarla dentro de otra funcion 

def increment(x):
  return x + 3

def high_ord_func(x, func):
  return x + func(x)

result = high_ord_func(2, increment)
#que el incremento seria 2 +(2 + 1)
print(result)

#haciendo el mismo ejemplo preo con lamda
def increment(x):
  return x + 3
increment_2 = lambda x: x + 2

def high_ord_func(x, func):
  return x + func(x)
high_ord_func_2 = lambda x, func: x + func(x)# parametros de entrada y salida 

result = high_ord_func(4, increment)
#que el incremento seria 2 +(2 + 1)
print(result)

result = high_ord_func_2(2, increment_2)#con esta linea de codigo que seria la definicion que seria la lambda de funtions, podria estra cambiandola  muy dinamicamnte y sin necesidad de de definirla o asignarla a una variables
print(result)
result = high_ord_func_2(2, lambda x: x + 20)
print(result)
result = high_ord_func_2(2, lambda x: x * 50)
print(result)
#el objectivo de las lambda es que no necesitamos definir el def en diferentes partes de la estructura de nuetro codigo 

def increment(x):
  return x + 2

increment_v2 = lambda x : x + 4

def hof(x, func):
  return x + func(x)

hof_v2 = lambda x, func : x + func(x)

result = hof(4, increment)

print(result)

re_result = hof(4,increment_v2)

print(re_result)

re_result_v2 = hof(2,lambda x : x + 10)
re_result_v3 = hof(2,lambda x : x * 15)
re_result_v4 = hof(2,lambda x : x * 21)
print(re_result_v2)
print(re_result_v3)
print(re_result_v4)