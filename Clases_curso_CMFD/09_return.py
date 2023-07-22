#===>>> retornando valoresres de nuetras funciones 
def find_volumen(altura, ancho, profundida):
  return altura * ancho * profundida

result = find_volumen(10, 20, 30)#===>>> aca estamos indicado que esta funcion deberia estar retornando tres parametros (altura, ancho, profundida )
print(result)
print('#' * 50)
#===>>> definiendo parametros con valores por defecto 
def find_volumen(altura=10, ancho=10, profundida=10):#en esta funcion solo me retornara lo que estoy asignando a cada parametro 
  return altura * ancho * profundida

result = find_volumen()
print(result)

print('*' * 50)
#retornando solo el valor que le asigno
def find_volumen(altura=10, ancho=20, profundida=30):
  return altura * ancho * profundida

result = find_volumen(altura=20)#==>solo retornara este valor asignado 
print(result)
#===>>> en todas estas funciones solo nos retorna una funcion y nos devuelve ese vaolr como resultado, pero en python podemos retornar mas de una funcion

print("#" * 50)
#===>>> retornando mas de una funtion 
def find_volumen(altura=10, ancho=20, profundida=30):
  return altura * ancho * profundida, ancho, 'hola emanuel, nico'

result = find_volumen(ancho=20)
print(result)
#==>> al ejecutar esta funcion octendremos uana tupla con esos valores asignados (def find_volumen(altura, ancho, profundida)

def find_volumen(altura=10, ancho=20, profundida=30):
  return altura * ancho * profundida, ancho, 'hola emanuel, nico'

result, ancho, texto = find_volumen(ancho=20)
print(result)
print(ancho)
print(texto)
#==>> como podemos natar una funcion puede retornar multiples valores, y asignar valores por defecto a esa entradas 