
from clases import Tablero
from funciones import pedir_coordenada

print("Let's start the game!")

jugador = Tablero("Jugador")
ordenador = Tablero("Ordenador")

jugador.colocar_flota_aleatoria()
ordenador.colocar_flota_aleatoria()

print("Player's board:")
for fila in jugador.tablero:
    print(fila)

print("Computer's board:")
for fila in ordenador.tablero:
    print(fila)


print("Your turn!")

fila = pedir_coordenada()
columna = pedir_coordenada()

print("DEBUG:", repr(jugador.disparos[fila][columna]))
resultado = jugador.disparar(fila, columna, ordenador)

if resultado == "hit":
    print("Hit!")
elif resultado == "miss":
    print("Miss!")
else:
    print("You have already shot at this cell. Choose another one!")
