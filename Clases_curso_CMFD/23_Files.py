#en esta clase trabajaremos con archivos. como leer los archivos txt archivos de texto plano.
file = open('./Clases_curso_CMFD/Texto.txt')# con open podemos abrir los archivos 
#print(file.read()) #y aca, lo imprimimos y lo leemos  

print('#'* 50)
#tambien podemos leer ese texto plana linea a linea 
'''print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())'''
 #tambien es muy importante cerrar ese archivo despues de usarlo para liverar memoria en la la ram 

for line in file:
  print(line)

file.close()

with open('./texto.txt') as file:
  for line in line:
    print(line) #esta es la forma mas cotiniana de serra leer un archivo y despues de que lo leamos el se cerrara automativamente


'''
También es recomendable usar esta estructura para que no aparezcan símbolos raros encaso de que se sean archivos binarios.
‘r’ = para leer el archivo
’encoding="UTF-8’ = convierte todo en letras
with open("./archivos/numbers.txt", "r", encoding="UTF-8") as f:

'''
