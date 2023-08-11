'''En Python, un módulo es un archivo que contiene definiciones de funciones, clases y variables que se pueden utilizar en otros programas. 
Los módulos permiten organizar el código en archivos separados para facilitar su reutilización y mantenimiento.'''

#Existen dos tipos principales de módulos en Python:

## Módulos incorporados: 
'''
Son módulos que vienen incluidos en la instalación estándar de Python y pueden ser utilizados directamente sin necesidad de instalar o 
importar nada adicional. Algunos ejemplos de módulos incorporados son math, random, datetime, os, entre otros.'''

## Módulos externos: 
'''
Son módulos desarrollados por la comunidad de Python o por terceros, que no vienen incluidos en la instalación estándar. 
Para utilizar estos módulos, es necesario instalarlos primero utilizando herramientas como pip 
y luego importarlos en el programa que los utilizará.'''

'''
Para utilizar un módulo en Python, primero debemos importarlo. 
El comando import se utiliza para cargar un módulo incorporado o externo en nuestro programa. '''

##Por ejemplo:

import math
import random
import datetime
#Luego de importar un módulo, podemos utilizar sus funciones y clases utilizando la sintaxis nombre_del_modulo.nombre_de_la_funcion.

## Ejemplo de uso de módulos incorporados:

import math

# Utilizando la función sqrt del módulo math para calcular la raíz cuadrada
num = 25
raiz_cuadrada = math.sqrt(num)
print("La raíz cuadrada de", num, "es", raiz_cuadrada)

# Utilizando la constante pi del módulo math para calcular el área de un círculo
radio = 5
area_circulo = math.pi * radio ** 2
print("El área del círculo de radio", radio, "es", area_circulo)

## Ejemplo de uso de módulos externos:

# pip install requests
'''
Supongamos que queremos utilizar el módulo requests para realizar peticiones HTTP en nuestro programa. 
Primero, debemos instalar el módulo utilizando pip:'''



'''

Luego, en nuestro programa, podemos importar el módulo y utilizar sus funciones:'''

'''
import requests

# Realizando una petición GET a una API
response = requests.get("https://api.example.com/data")
if response.status_code == 200:
    data = response.json()
    print("Datos obtenidos:", data)
else:
    print("Error en la petición:", response.status_code)
    
    '''

'''
En resumen, los módulos en Python son una poderosa herramienta para organizar y reutilizar el código. 
Los módulos incorporados son parte de la instalación estándar de Python y están listos para ser utilizados, 
mientras que los módulos externos deben ser instalados primero y luego importados en el programa. 
Con los módulos, podemos acceder a una amplia variedad de funcionalidades y recursos disponibles en la comunidad de Python.'''