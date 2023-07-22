#union de conjuntos 
set_a = {'colombia', 'brazil', 'argentina', 'ecuador'}
set_b = {'volivia', 'peru', 'venezuela', 'argentina', 'colombia'}
set_c = set_a.union(set_b)
print(set_c)
print('*' * 40)
#intersecion de conjuntos donde en un subconjunto aparece el elemento que tienen en comun ambos conjuntos 
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#diferencia entre dos conjuntos 
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#diferencia simetrica los elementos de los conjuntos que no tienen nada en comun
set_c = set_a.symmetric_difference(set_b)
print(set_c)