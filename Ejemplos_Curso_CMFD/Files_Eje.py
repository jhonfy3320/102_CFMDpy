'''
Leer un archivo de texto en Python es un proceso sencillo. 
Puedes utilizar el siguiente código como ejemplo para leer un archivo de texto línea por línea:'''

# Abrir el archivo en modo lectura
nombre_archivo = "Ejemplos_Curso_CMFD/Texto_Eje.txt"  # Reemplaza "archivo.txt" con el nombre de tu archivo
with open(nombre_archivo, "r") as archivo:
    # Leer y mostrar cada línea del archivo
    for linea in archivo:
        print(linea.strip())  # strip() elimina los espacios en blanco y saltos de línea al final de cada línea

'''
En este ejemplo, estamos usando la instrucción with open() para abrir el archivo en modo lectura ("r"). 
Esto asegura que el archivo se cerrará automáticamente después de su uso.

Luego, usamos un bucle for para iterar sobre cada línea del archivo y utilizamos print() para mostrar cada línea en la consola. 
La función strip() se utiliza para eliminar espacios en blanco y saltos de línea al final de cada línea leída.

Si deseas leer todo el contenido del archivo como una sola cadena en lugar de línea por línea, puedes usar el método read():
'''
nombre_archivo = "archivo.txt"
with open(nombre_archivo, "r") as archivo:
    contenido = archivo.read()

print(contenido)

'''
En este caso, contenido contendrá todo el contenido del archivo como una única cadena.

Recuerda reemplazar "archivo.txt" con el nombre de tu propio archivo de texto que deseas leer.'''