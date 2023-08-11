#en esta clase aprenderemos sobre el manejo y control de los errores en python 


#print(0/0)#nosostros podemos manejar y controlar este error mapar que el programa no se me detenga y las 
#demas lineas que no tienen error no se detengan y se ejecuten a la perfeccion 

#print('hola mundo como estas el dia de hoy dios ')

try:
  print(0/0)
except ZeroDivisionError as error:
  print(error) # con este bleuqe de codigo podemos excepcioner ese error con la ayuda de try y 
  #excep, todo error que ocurra dentro de este bloque lo podemos capturar, y podemos hacer lo queramos con el, 
  # y con el print puedes lanzar un alerta del error 
try:
  assert 1 != 1, 'uno no diferente de uno'
except AssertionError as error:
  print(error)
try:
  edad = 19
  if edad > 18:
    raise Exception('en mi programa no se permiten mayores de edad')
except Exception as error:
  print(error)

print('hola mundo como estas el dia de hoy dios ')

#podemos unificar estos errores en uno solo 

try:
  print(0/0)
  assert 1 != 1, 'uno no diferente de uno'
  edad = 19
  if edad > 18:
    raise Exception('en mi programa no se permiten mayores de edad')
    #aca tenemos el bloque de codigo, que puede generar el error 
except ZeroDivisionError as error:
  print(error, 'en este caso zero no de puede dividir en zero')
except AssertionError as error:
  print(error)
except Exception as error:
  print(error) #Y aca estamo capturando cada uno de esos errores 

print('hoy depronto me veo con nico ojala ocurra ')
print('si ocurrio y fue muy chevere y muy hermoso ')
print('*#' * 40)
print('nico emanuel')
print('me hacen tanta falta quiciera esra co ellos hay y abrazarlos muy fuertemente ')