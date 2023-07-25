'''
Para resolver el desafío, utilizaremos la función map() junto con una función lambda para multiplicar cada número de la lista por dos y 
retornar una nueva lista con los resultados.'''

def multiplicar_numbers(numbers):
    #Utilizamos map() para aplicara la funcion lambda a cada numero de la lista
    #La funcion lambda multiplicara cada numero por dos 
    result = list(map(lambda x: x * 12, numbers))
    return result

# Ejemplos de uso 
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = multiplicar_numbers(lista_numeros)
print(resultado)


'''
En este ejemplo, definimos la función multiply_numbers() que toma una lista numbers como argumento. 
Utilizamos map() junto con la función lambda lambda x: x * 2 para aplicar la operación de multiplicar por dos a cada número de la lista. 
El resultado se almacena en la variable result, que es una lista con los números transformados.'''

'''
Luego, llamamos a multiply_numbers() con la lista lista_numeros y almacenamos el resultado en la variable resultado. 
Al imprimir resultado, obtenemos la lista transformada con cada número multiplicado por dos.

La función map() es una forma eficiente y concisa de aplicar una misma operación a todos los elementos de una lista y obtener una nueva 
lista con los resultados. 
La función lambda nos permite definir la operación directamente en el lugar donde se usa, lo que hace que el código sea más claro y legible.'''




