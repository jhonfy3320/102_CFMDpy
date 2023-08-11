import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./Clases_curso_CMFD/app/data.csv')
  print(data)


'''
import csv: 
Esta línea importa el módulo csvde Python, que proporciona funciones para leer y escribir archivos CSV (Comma-Separated Values).

def read_csv(path):: 
Esto define una función llamada read_csvque toma un argumento pathque representa la ruta del archivo CSV que se va a leer.

with open(path, 'r') as csvfile:: 
Abre el archivo CSV especificado en modo de lectura ( 'r') usando un bloque with. 
Esto garantiza que el archivo se cierre correctamente después de su uso.

reader = csv.reader(csvfile, delimiter=','): 
Crea un objeto lector CSV llamado readerque utiliza la coma como delimitador para separar los campos en cada fila.

header = next(reader): 
Lee la primera fila del archivo CSV y la asigna a la variable header. Esto se supone que contiene los nombres de las columnas.

data = []: 
Inicializa una lista vacía llamada dataque se ocupa para almacenar los datos del archivo CSV en forma de diccionarios.

for row in reader:: 
Inicia un bucle que itera sobre las filas restantes del archivo CSV.

iterable = zip(header, row): 
Crea un objeto iterable que combina cada elemento del encabezado con el valor correspondiente en la fila real.

country_dict = {key: value for key, value in iterable}: 
Crea un diccionario llamado country_dictutilizando la comprensión de diccionarios. 
Asocia cada elemento del encabezado con el valor correspondiente en la fila, creando así un diccionario de datos para una fila específica.

data.append(country_dict): Agrega el diccionario country_dicta la lista data.

return data: Devuelve la lista completa de diccionarios que representan los datos del archivo CSV.

if __name__ == '__main__':: 
Esta línea verifica si el script se está acabando como el programa principal.

data = read_csv('./Clases_curso_CMFD/app/data.csv'): 
Llama a la función read_csvpara leer el archivo CSV en la ruta especificada y almacena los datos en la variable data.

print(data[0]): 
Imprime el primer diccionario de la lista data, que corresponde a los datos de la primera fila del archivo CSV.

En resumen, este bloque de código define una función read_csvque lee un archivo CSV y devuelve los datos en forma de una lista de diccionarios, 
donde cada diccionario representa una fila con columnas correspondientes. 
Luego, en la parte if __name__ == '__main__':, se llama a esta función para leer un archivo CSV específico y se imprime la primera fila de datos.'''