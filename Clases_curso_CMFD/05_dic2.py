'''dic = {}
for i in range(1, 21):
  dic[i] = i * 4
  print(dic)''' #generando diccionarios para l comprecion llaves con un iterador en este caso llegando hazta 20, y cada que itera lo multiplicara por 4

'''dic_2 = {i: i * 4 for i in range(1, 21) }
print(dic_2)'''#etamos generando diccionarios pero con una sintaxys mas corta 

import random#random nos ayuda a dar un valor de poblacion a cada pais de forma aleatoria
countries = ['col', 'cosr', 'bra', 'ecu','vol','usa','per']
population = {}
for country in countries:
  population[country] = random.randint(1, 1000) #aca estamos generando la poblacion de cada pais aleatoriamnet, en un rango de 1 a 1000
print(population)

population_2 = {country: random.randint(1, 1000) for country in countries}
print(population_2) #aca estamos generando la asignacion de poblacion aleatoriamente a cada pais pero de una forma mas aleatoriamente 

#generando listas y uniendolas 
nombres = ['emanuel', 'nico','martin', 'sebastian', 'juan jose']
edades = [12, 12, 6, 7,6]
print(list(zip(nombres, edades))) #con zip podemos unir listas, de una forma muy facil y cencilla. En la consolas nos imprimira una tupla de cada uno de los valores de las listas 

new_dic = {nombre: edad for (nombre, edad) in zip(nombres, edades)}
print(new_dic)#para general un diccionario con las tuplas debemos poner las llaves clave valor, que seria nombres y edades, para unir las listas, como podemos ver es una forma muy cencilla de unir listas 

names = ['nico', 'zule', "santi"]
edades = [12,56,98]
new_dict = {names[i]:edades[i] for i in range(len(names))} 
print(new_dict) #aca estamos generando un diccionario con las tuplas 