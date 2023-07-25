# en esta clase aprenderemos sobre map que su principal funcion es hacer transformaciones a una lista de elementos, si en la lista tienes 8 elementos, si los transformamos obtendremos los mismos 8 elementos pero transformados 
#MAP ====>>> es una de las funciones mas usadas en el dia a dia como cientifico de datos 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = []
for i in numbers:
  numbers_2.append(i * 4)
  
print(numbers)
print(numbers_2)

#haciendo todo el codigo anterior mas simple y en una linea 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = []
for i in numbers:
  numbers_2.append(i * 4)
print('#' * 50)
numbers_3 = list(map(lambda i: i * 6, numbers)) # aca estamos usando map que es una funcion preconstruida de python, y no es necesario definirla la funcion se la puedo emviar como una lambda tranformandolo en una lista 
  
print(numbers)# nos imprimira la lista que le asignamos 
print(numbers_2)#imprimira esa lista con los mismo elementos pero transformados 
print(numbers_3)#aca obtenemos los mismos elementos transformados pero en una sola linea de codigo 

#trabajando con map en listas de diferentes dimenciones 
numbers1_1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numbers1_2 = [21, 22, 23, 24, 25, 28, 33, 42, 51, 33]
print(numbers1_1)
print(numbers1_2)

numbers2_1 = list(map(lambda x, y: x + y, numbers1_1, numbers1_2 ))
print(numbers2_1)#aca nos esta tranformando cada lista, iterando cada lista y sumando los valores con respecto a la lista mas pequeña, y aplica la lamda 
