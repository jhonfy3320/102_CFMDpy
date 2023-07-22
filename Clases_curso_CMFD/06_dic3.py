import random  #random nos ayuda a dar un valor de poblacion a cada pais de forma aleatoria
countries = ['col', 'cosr', 'bra', 'ecu','vol','usa','per']

population_2 = { country: random.randint(1, 1000) for country in countries}
print(population_2)

result = {country: population for (country, population) in population_2.items() if population > 600 }
print(result)

#iterando una cadena de caracteres 
text = 'hola soy emnuel, y yo nico, tenemos 12 años'
unique = {y: y.upper() for y in text if y in 'aeiou'}
print(unique)#tenemos que general nuetra llave clave valor
#como podemos notar nos imprime solo la lleve valor, que en este caso es la vocal, y lo imprime en mayusculas 

text = 'hola soy emnuel, y yo nico, tenemos 12 años'
unique = {y: y.count(y) for y in text if y in 'aeiou'}
print(unique)

def run():
    text = "Hola a todos, esta es una cadena de texto de prueba."
    print(text)
    unique = { c: text.count(c) for c in text if c in 'aeiou' }
    print(f"unique: {unique}")

if __name__ == '__main__':
    run() #con esta franja de codigo estamos imprimiendo cuantas veces se encuantra cada vocal en el texto 


