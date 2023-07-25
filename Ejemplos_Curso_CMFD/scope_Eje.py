'''
El scope o alcance en Python se refiere a la accesibilidad de variables, funciones y otros objetos en diferentes partes de un programa. 
Cada variable en Python tiene un alcance que define dónde puede ser accedida y utilizada dentro del código. 
Entender el scope es importante para evitar conflictos de nombres, asegurarse de que las variables sean utilizadas donde corresponde 
y comprender cómo funcionan las funciones.'''

#Python tiene tres tipos principales de alcance:

## Global Scope (Alcance global):

'''
Las variables declaradas fuera de cualquier función o bloque de código tienen un alcance global. 
Estas variables son accesibles desde cualquier parte del programa, incluidas todas las funciones. 
Para definir una variable global, se debe declarar fuera de cualquier función o bloque, en el nivel más alto del programa.'''

# Ejemplo de alcance global:


x = 10  # Variable global

def funcion():
    print(x)  # x es accesible aquí porque es una variable global

funcion()  # Salida: 10

## Local Scope (Alcance local):
'''
Las variables declaradas dentro de una función tienen un alcance local. 
Estas variables solo son accesibles dentro de la función en la que fueron definidas y no están disponibles fuera de ella. 
Una vez que la función termina su ejecución, las variables locales se destruyen.'''

## Ejemplo de alcance local:

def funcion():
    y = 5  # Variable local
    print(y)

funcion()  # Salida: 5
# print(y)  # Generaría un error ya que "y" es una variable local y no es accesible aquí

## Nonlocal Scope (Alcance no local):

'''
El alcance no local es relevante para funciones anidadas, es decir, funciones definidas dentro de otras funciones. 
Si una variable se define en una función exterior y se quiere modificar o acceder desde una función interna, 
se puede utilizar la declaración nonlocal para indicar que esa variable no es local a la función interna.'''

## Ejemplo de alcance no local:

def exterior():
    z = 10  # Variable local a "exterior"

    def interior():
        nonlocal z  # Indicamos que "z" no es local a "interior"
        z += 5
        print(z)

    interior()

exterior()  # Salida: 15

'''En este ejemplo, la variable z está declarada en la función exterior, pero también es utilizada y modificada en la función anidada interior. 
Utilizamos nonlocal z en la función interior para indicar que la variable z no es local a esta función y que se refiere a la variable z de la 
función exterior.'''

'''
Es importante tener en cuenta el alcance de las variables para evitar confusiones y comportamientos inesperados en el código. 
El uso adecuado del scope asegura que las variables sean accesibles donde se necesitan y ayuda a mantener el código más claro y organizado.'''