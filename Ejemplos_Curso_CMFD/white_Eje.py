'''
Escribir en un archivo en Python es un proceso sencillo. 
Puedes utilizar el siguiente código como ejemplo para escribir contenido en un archivo de texto:'''

# Abrir el archivo en modo escritura (si no existe, se crea; si existe, se sobrescribe)
nombre_archivo = "nuevo_archivo.txt"  # Reemplaza "nuevo_archivo.txt" con el nombre que desees
contenido = "Este es el contenido que quiero escribir en el archivo.\n"

with open(nombre_archivo, "w") as archivo:
    archivo.write(contenido)

print("Contenido escrito en el archivo:", contenido)

'''
En este ejemplo, estamos usando la instrucción with open() para abrir el archivo en modo escritura ("w"). 
Esto crea un archivo llamado "nuevo_archivo.txt" (puedes cambiar el nombre) si no existe, o sobrescribe el contenido del archivo si ya existe.

Luego, utilizamos el método write() del objeto de archivo para escribir el contenido en el archivo. 
El contenido incluye una cadena de ejemplo y un salto de línea ("\n") para que el próximo contenido se escriba en una línea nueva.

Recuerda que si el archivo ya existe y usas el modo de escritura "w", su contenido anterior se sobrescribirá. 
Si deseas agregar contenido al final del archivo sin eliminar el contenido existente, puedes usar el modo de escritura y agregado "a" 
en lugar de "w".

Asegúrate de reemplazar "nuevo_archivo.txt" con el nombre que desees para el archivo y modificar el contenido según tus necesidades.'''