import csv

def read_csv(path):
   total = 0
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for row in reader:
         total += int(row[1])
   return total

response = read_csv('Retos Playgrounds/LeeunCSVpara_calcular_el_total_gastos/data.csv')
print(response)