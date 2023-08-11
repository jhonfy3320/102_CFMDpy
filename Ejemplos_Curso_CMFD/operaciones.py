'''
Crear nuestros propios módulos en Python es una excelente manera de organizar y reutilizar nuestro código en diferentes programas. 
Un módulo personalizado es simplemente un archivo de Python con extensión 
.py que contiene definiciones de funciones, clases y/o variables que queremos utilizar en otros programas.'''

'''
Para crear nuestro propio módulo, simplemente creamos un archivo con el código que queremos incluir, y luego podemos importarlo en 
otros programas como lo haríamos con un módulo incorporado o externo.'''

## Vamos a ver un ejemplo paso a paso de cómo crear y utilizar un módulo personalizado:

## Paso 1: Crear el módulo
'''
Supongamos que queremos crear un módulo llamado operaciones que contiene algunas funciones matemáticas simples, como suma y resta.

Creamos un archivo llamado operaciones.py con el siguiente contenido:'''

# operaciones.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

'''
Paso 2: Utilizar el módulo en otro programa
Ahora, crearemos otro programa llamado main.py en el mismo directorio donde tenemos nuestro módulo operaciones.py. 
En este programa, importaremos el módulo operaciones y utilizaremos las funciones que definimos en él.'''

# main.py

# Importamos nuestro módulo personalizado
import operaciones

# Utilizamos las funciones del módulo
resultado_suma = operaciones.suma(10, 5)
resultado_resta = operaciones.resta(10, 5)

print("Resultado de la suma:", resultado_suma)
print("Resultado de la resta:", resultado_resta)

'''
Paso 3: Ejecutar el programa
Para ejecutar el programa main.py, simplemente abrimos una terminal o línea de comandos, nos ubicamos en el 
directorio donde se encuentran los archivos operaciones.py y main.py, y escribimos:'''

'''
python main.py
La salida será:

Resultado de la suma: 15
Resultado de la resta: 5
En resumen, crear nuestros propios módulos en Python es tan sencillo como definir funciones y clases en un archivo 
.py, y luego importarlo en otros programas donde necesitemos utilizar esas definiciones. 
De esta manera, podemos reutilizar nuestro código de manera eficiente y organizar nuestras funciones y clases en módulos 
para mantener nuestro código limpio y modular.'''