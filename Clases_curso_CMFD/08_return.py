#en esta clase miraremos el retorno de valores 
'''sum = 0 
for x in range(1 ,20): 
  sum += x
print(sum)''' #este bloque de codigo iterara del 1 a 20 t los sumara 

def sum_with_range():
  sum = 0 
  for x in range(1 ,20): 
    sum += x
  print(sum)

sum_with_range()
sum_with_range()

print('#' * 60)
#mejorando nuetra funcion 
def sum_with_range(min, max):
  sum = 0 
  for x in range(min ,max): 
    sum += x
  print(sum)

sum_with_range(1, 20)
sum_with_range(21, 40)
sum_with_range(40, 100)
#nuetra funcion es mas dinamica y estamos reutilizando codigo, estos nos quiere decir que reutilizamos esa funcion 

print('*' * 60)
print('# ===>> las funciones tambiem pueden retornar un valor ')
def sum_with_range(min, max):
  print(min, max)
  sum = 0 
  for x in range(min ,max): 
    sum += x
  return sum #==>> aca estamos retornando el valor de nuetra funcion 

result = sum_with_range(1, 20)
print(result)
result_2 = sum_with_range(result, result + 40)
print(result_2)
result_3 = sum_with_range(result, result + 100)
print(result_3)# ==>> lo que hacemos aca esque cada ves que ejecutemos la funcion nos retornara el resultado anterior y lo sumara el valorque le estamos asignando 