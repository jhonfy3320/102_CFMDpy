#modificacion de los conjuntos con diferentes comandos, que nos ayudaran a modificar, cambiar o agrera elementos de los conjuntos 

set_contries = {'colombia', 'mexico', 'usa', 'canada', 'volivia', 'ecuador'}
print(set_contries)
size = len(set_contries)
print(size)

print('colombia' in set_contries)
print('egit' in set_contries)

# ADD ==>> agregar un nuevo elemento al conjunto 
set_contries.add('brazil')
print(set_contries)
set_contries.add('brazil')
print(set_contries)

#tambien podemos actualizar elementos de nuetros conjuntos de elementos 
#UPDATE
set_contries.update({'ecuador', 'pero', 'colombia'})
print(set_contries)

#tambiem podemos remover datos de los conjuntos 
set_contries.remove('ecuador')
print(set_contries)

#si por equivocacion queremos borrar un archivo que no se encuentra en los conjuntos, no arrojara y typeerror, para evitar esta clase de incomendinte usamos (discar)
set_contries.discard('japon')
print(set_contries)
set_contries.add('japon')
print(set_contries)

#si queremos eliminar todo lo que tenemos en el conjunto lo hacemos con (clear)
set_contries.clear()
print(set_contries)
print(len(set_contries))


