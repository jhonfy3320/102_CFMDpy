'''Voy a refactorizar el juego de piedra, papel o tijera en Python para hacerlo más conciso y organizado. 
Utilizaré un diccionario para mapear las opciones del juego y una función para determinar el resultado de cada ronda.'''


import random

def game(player_choice):
    choices = {
        'piedra': 'tijera',
        'papel': 'piedra',
        'tijera': 'papel'
    }

    computer_choice = random.choice(['piedra', 'papel', 'tijera'])

    print(f"Tú eliges: {player_choice}")
    print(f"La computadora elige: {computer_choice}")

    if player_choice == computer_choice:
        print("Empate")
    elif choices[player_choice] == computer_choice:
        print("¡Ganaste!")
    else:
        print("La computadora gana")

if __name__ == "__main__":
    print("¡Bienvenido al juego Piedra, Papel o Tijera!")
    player_choice = input("Elige piedra, papel o tijera: ").lower()

    if player_choice not in ['piedra', 'papel', 'tijera']:
        print("Opción inválida. Por favor, elige entre piedra, papel o tijera.")
    else:
        game(player_choice)
'''
En este código, utilizo un diccionario llamado choices para mapear las opciones del juego. 
Las llaves representan las elecciones posibles del jugador, y los valores correspondientes representan las elecciones que vencen a la 
opción del jugador. 
Luego, utilizo la función random.choice() para que la computadora elija una opción aleatoria entre piedra, papel o tijera.

La función game(player_choice) recibe la elección del jugador como argumento y compara con la elección de la computadora para determinar 
el resultado de la ronda. 
Finalmente, el programa pregunta al jugador su elección y muestra el resultado de la ronda.

El código es más conciso y fácil de entender con este refactor. 
Además, se asegura de que el jugador ingrese una opción válida y le brinda retroalimentación sobre el resultado del juego.'''