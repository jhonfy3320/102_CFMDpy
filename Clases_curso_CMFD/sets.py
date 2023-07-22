set_contries = {'col', 'mex', 'usa', 'can', 'volivia', 'ecuador'}
print(set_contries)
print(type(set_contries))#estos son conjutos, (set), son muy parecido a los diccionarios, en un conjunto no pueden haber elementos repetidos
#En nuetro conjunto podemos tener elementos repetidos, pero a la hora de imprimirlos enla consola no apareceran repetidos 
set_numbers = {1, 2, 4, 4, 5, 6, 7, 8, 0, 12, 11, 11, 2, 5, 15}
print(set_numbers)
print(type(set_numbers))#conjunto de numeros 

set_type = {'nico', 'emanuel', True, 33, False, 33, 'hola', 12.34}
print(set_type) # conjunto con diferentes elementos, al imprimir en consolo daran otro orden pero no habra ningon ploblema 

#conjunto con string 
set_from_string = set('hola mundo mundo')
print(set_from_string)#al imprimir en consola no nos mostrara los string repetidos 

#tambien los podemos general con tuplas 
set_from_tuples = set(('nicolas', 'emanuel', 'senastian', 'martin', 'emanuel'))
print(set_from_tuples)# como podemos notar las tuplas tambien las pasa a conjuntos
numbers = [1,2,3,4,5,6,7,8,9,0,10,1,2,3,4,5,6,7,8,9,0,10,]
set_numbers = set(numbers)
print(set_numbers)#esta definido como una lista pro aca lo pasamos a un conjotos. Ademas nos imprimira los numeros unicos no los repetidos 

#esta lista de numeros unicos tambien lo podemos pasar a una lista
unico_numbers = list(set_numbers)
print(unico_numbers)

#En esta clase tuvimos el primer acercamiento a los conjuntos, pero podemos parender mucho mas de llos y para que son utiles 
