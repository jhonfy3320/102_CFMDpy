#ESCRIBIR TEXTOS EN PYTHON
#Para poder escribir texto en python solo debemos agregar al parámetro open( ) algunas de las siguientes reglas
with open('./texto.txt', 'r+') as file: # con (r+)rpluz damos permiso para lectura y escritura de un archivo 
  for line in file:
    print(line)

  file.write('estamos agregando nuevas cosa a estos Archivo hola chicos como estan\n') 
  file.write('que hacen de nuevo emanuel lo estraño mucho\n')  
  file.write(' ayer me pude ver con nico un buen rato y la pasamos muy chever ') #aca estamos agregando, los nuevos comentarios al archivo atrevez de los permisos 
#con (\n podemos hacer saltos lineas entre textos )

'''with open('./texto.txt', 'w+') as file:''' # con (w+) demos permiso de escritura y lectura pero cuando hacemos una modifecacion en el erchivo lo sobre escriviomos y cambiamos todo lo que hay en el 