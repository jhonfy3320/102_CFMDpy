'''
Para resolver el desafío, necesitas completar la función get_total en el archivo main.py utilizando las funciones definidas en my_functions.py. 
Aquí tienes la implementación:'''

from my_functions import get_totals, calc_total

def get_total(orders):
    totals = get_totals(orders)
    total_sum = calc_total(totals)
    return total_sum

orders = [
    {
        "customer_name": "Nicolas",
        "total": 100,
        "delivered": True,
    },
    {
        "customer_name": "Zulema",
        "total": 120,
        "delivered": False,
    },
    {
        "customer_name": "Santiago",
        "total": 20,
        "delivered": False,
    }
]

total = get_total(orders)
print(total)
