#==>>alacance de nuetras funciones a nivel gloval 
price = 200 #==> nuetra funcion global 
def increment():
  price = 200 # aca price solo tiene un contexto local 
  price = price + 20
  print(price)
  return price

print(price)
price_2 = increment()
print(price_2)
  
#==> como podemos notar hay dos funciones pero ambas tinen contextos diferentes, segun lo asignado global o local 

print('#' * 50)
#===>>> evitando el choque de funciones, llamando uan funncion que no tiene un contexto definido 
'''price = 200
def increment():
  price = 200
  result = price + 20
  print(result)
  return result

print(price)
price_2 = increment()
print(price_2)
print(result)'''#aca nos arrojaria un error y chocarian porque result no esta definido globalmente

price = 200
result = 200
def increment():
  price = 200
  result = price + 20
  print(result)
  return result

print(price)
price_2 = increment()
print(price_2)
print(result)

print('#*' * 50)
'''('Creo que esto te puede ayudar a entender mejor: Dentro de una función puede haber variables, las cuales se llaman variables locales. Estas variables locales, se identifican porque están escritas dentro de la definición de la función; y únicamente funcionan mientras que la función sea llamada o utilizada. Si vas a llamar a una variable local por fuera de la función, no servirá.
Y existen variables globales, que son las que están escritas fuera de una función. Estas variables si funcionan al ser llamadas sin la función, porque no están determinadas dentro de la función.')'''
###############################################################
'''Exactamente. Creo que las palabras usadas no son las adecuadas y se presta para confusiones. De manera simple se entiende que las variables se pueden definir como globales, es decir, fuera de las funciones y locales, es decir, que solo son creadas dentro de esa función especifica y si es llamada fuera de ese bloque de codigo (me refiero a la variable local), pues no dara resultado porque simplemente no existe.'''