'''
La función get_totalutiliza las funciones get_totalsy calc_totaldefinidas en my_functions.py
para obtener la lista de montos de las órdenes de compra y luego calcular la suma total de todas las órdenes. 
Finalmente, el resultado se imprime en la consola.'''

def get_totals(orders):
    return [order['total'] for order in orders]

def calc_total(totals):
    return sum(totals)


'''
El resultado del ejemplo proporcionado será:

240
Esto representa la suma total de los montos de todas las órdenes de compra en la lista orders.'''
