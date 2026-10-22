# Importamos la clase Tablero del archivo clases.py (para crear y guardar tableros de jugadores con disparos).
from clases import Tablero
# Importamos la función que solicita las coordenadas.
from funciones import pedir_coordenada
# Importamos el módulo para generar números aleatorios (los disparos de ordenador).
import random

print("Welcome to Battleship!")

# Creamos el tablero del jugador y el del ordenador.
# La clase Tablero está definida en el archivo clases.py.
jugador = Tablero("Jugador")
ordenador = Tablero("Ordenador")

# Colocamos aleatoriamente los barcos en ambos tableros.
# El método colocar_flota_aleatoria() está definido en clases.py.
jugador.colocar_flota_aleatoria()
ordenador.colocar_flota_aleatoria()


# Mostramos la flota del jugador en la pantalla.
# El atributo tablero pertenece a la clase Tablero, definida en clases.py.
print("Your fleet:")

# Recorremos todas las filas del tablero de jugador.
for fila in jugador.tablero:
    print("+---" * 10 + "+") # (10 veces) Dibujamos la línea horizontal de la cuadrícula.
    print("| " + " | ".join(fila) + " |") #vertical
# Dibujamos el borde inferior del tablero.
print("+---" * 10 + "+") #abajo


# Iniciamos el bucle principal del juego.
while True:
    # Mostramos el mensaje para indicar el turno del jugador.
    print("Your turn to fire!")
    # Pedimos la coordenada de la fila.
    # La función pedir_coordenada() está definida en funciones.py.
    fila = pedir_coordenada()   
    
    # Si el jugador decide salir, terminamos el juego.
    if fila is None:
        break

    # Pedimos la coordenada de la columna.
    columna = pedir_coordenada()
    # Si el jugador decide salir, terminamos el juego.
    if columna is None:
        break

    # Realizamos un disparo en el tablero del ordenador.
    # El método disparar() está definido en clases.py.
    resultado = jugador.disparar(fila, columna, ordenador)
    
    # Comprobamos el resultado del disparo.
    if resultado == "hit":
        print("You hit a ship!")
    elif resultado == "miss":
        print("You missed!")
    else:
        # Si ya hemos disparado en esa casilla, pedimos otras coordenadas.
        print("You've already fired at these coordinates. Try again!")
        continue

    # Comprobamos si quedan barcos en el tablero del ordenador.
    quedan_barcos_ordenador = False
    # Recorremos todas las filas del tablero del ordenador.
    for fila in ordenador.tablero: 
        # Comprobamos cada casilla de la fila.
        for celda in fila:
            if celda == "🚢":
                quedan_barcos_ordenador = True

    # Si no quedan barcos, el jugador gana la partida.            
    if quedan_barcos_ordenador == False: 
        print ("Congratulations! You win!") 
        break
    # Si el jugador acierta, puede volver a disparar. 
    if resultado == "hit":
        continue

       
    # Mostramos el mensaje para indicar el turno del ordenador.
    print ("Computer's turn to fire!")
    
    # El ordenador elige unas coordenadas aleatorias.
    while True:
        # Generamos una fila y una columna aleatorias.
        fila_ordenador = random.randint(0, 9) 
        columna_ordenador = random.randint(0, 9) 
        
        # Comprobamos si el ordenador ya ha disparado en esa casilla.
        while ordenador.disparos[fila_ordenador][columna_ordenador] != " ":
            fila_ordenador = random.randint(0, 9) 
            columna_ordenador = random.randint(0, 9) 

        # El ordenador dispara al tablero del jugador.
        # El método disparar() está definido en clases.py.
        resultado_ordenador = ordenador.disparar(fila_ordenador, columna_ordenador, jugador)          
        
        # Comprobamos el resultado del disparo del ordenador.
        if resultado_ordenador == "hit":
            print ("The computer hit your ship!")
        elif resultado_ordenador == "miss":
            print ("The computer missed your ship!")
        else:
             # Si la casilla ya había sido seleccionada, elegimos otras coordenadas.
            print ("These coordinates have already been targeted. Try again!") 
            continue  
            
    
        # Mostramos los disparos del jugador contra el ordenador.
        print("Your shots at the computer:")
        for fila in jugador.disparos:
            print("+---" * 10 + "+")
            print("| " + " | ".join(fila) + " |")
        print("+---" * 10 + "+")

        # Mostramos los disparos del ordenador contra el jugador.
        print("Computer's shots at your board:")
        for fila in ordenador.disparos:
            print("+---" * 10 + "+")
            print("| " + " | ".join(fila) + " |")
        print("+---" * 10 + "+")

        # Comprobamos si quedan barcos en el tablero del jugador.
        quedan_barcos_jugador = False

        # Recorremos todas las filas del tablero del jugador.
        for fila in jugador.tablero: 
            # Comprobamos cada casilla de la fila.
            for celda in fila:
                if celda == "🚢":
                    quedan_barcos_jugador = True

        # Si no quedan barcos, el ordenador gana la partida.           
        if quedan_barcos_jugador == False: 
            print ("Game over! The computer wins!") 
            break
        # Si el ordenador falla, termina su turno.
        if resultado_ordenador == "miss":
            break

