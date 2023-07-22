'''numbers = []
for elemet in range(1, 21):
  numbers.append(elemet * 4)'''#se multiplica cada elemto de la iteracion por 4 en este caso
  
'''print(numbers) '''#estamos iterando una lista desde el 1 a 20 y la agregamos a element con appen 

'''numbers_f2 = [elemet *4 for elemet in range(1, 21)]''' #aca igual se estara multiplicando cada elemento de la iteracion 
'''print(numbers_f2)''' #en este codigo estamos, iterando la misma lista y agregandolo a element pero es mucho mas fasil de leer 
numbers = []
for i in range(1, 21):
  if i & 2 == 0: # condicional de si es = 0 lo agregara, si es impar lo inorara 
    numbers.append(i * 2)
print(numbers)

numbers_f2 = [i *4 for i in range(1, 21)if i & 4 == 0]
print(numbers_f2)
#toda esta sintaxis cumple la misma funcion que la que se hizo al principio, solo que son diferentes, y esta utima es mas facil de leer  

'''defsave_permut(a,b,c): 
if a >= 0and b >= 0and c >= 0:
    # lists of each value of element
    list_x = [i for i inrange(a+1) if i<=x]
    list_y = [j for j inrange(b+1) if j<=y]
    list_z = [k for k inrange(c+1) if k<=z]
    # Element distribution
    listPermut = [[i,j,k] for i in list_x for j in list_y for k in list_z]
    return listPermut
defremove(lista):
# removing
new_list = [i for i in lista if (i[0]+i[1]+i[2]) != n]
return new_list

if __name__ == '__main__':
x = int(input())
y = int(input())
z = int(input())
n = int(input())
#save the permutations
permut = save_permut(x,y,z)
#remove
result = remove(permut)
print(result)'''

