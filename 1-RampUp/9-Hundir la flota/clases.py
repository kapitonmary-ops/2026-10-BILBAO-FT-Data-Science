
import random
from variables import TAMANO_TABLERO, FLOTA

class Tablero:
    
    def __init__(self, player_id):
        #creamos un ID para cada jugador
        self.player_id = player_id
        #tablero propio: barcos y disparos del ordenador
        self.tablero = [[" " for j in range(TAMANO_TABLERO)] for i in range(TAMANO_TABLERO)]
        #disparos del jugador contra el ordenador
        self.disparos = [[" " for j in range(TAMANO_TABLERO)] for i in range(TAMANO_TABLERO)]
        #creamos copia de flota para tener dos distintos 
        self.flota = FLOTA.copy()
    def colocar_barco(self, fila, columna, longitud, orientacion):
#Definimos la dirección del barco       
        cambio_fila = 0
        cambio_columna = 0
        
        if orientacion == "H":
            cambio_columna = 1
        elif orientacion == "V":
            cambio_fila = 1
        else: 
            return False
                
#Comprobamos todas las casillas del barco antes de colocarlo
        for i in range(longitud):
            nueva_fila = fila + i * cambio_fila
            nueva_columna = columna + i * cambio_columna
            
#Comprobamos que la casilla está dentro del tablero
            if (nueva_fila < 0 or nueva_fila >= TAMANO_TABLERO or nueva_columna < 0 
                    or nueva_columna >= TAMANO_TABLERO):
                return False

#Comprobamos que la casilla está libre
            if self.tablero[nueva_fila][nueva_columna] != " ":
                return False
            
        
#Si todas las casillas están libres, colocamos el barco
        for i in range(longitud):
            nueva_fila = fila + i * cambio_fila
            nueva_columna = columna + i * cambio_columna
            self.tablero[nueva_fila][nueva_columna] = "B"

        return True  #Barco colocado correctamente
    
    
    def colocar_flota_aleatoria(self):
        for nombre, longitud in self.flota.items():
            colocado = False

            while not colocado:
                fila = random.randint(0, TAMANO_TABLERO - 1)
                columna = random.randint(0, TAMANO_TABLERO - 1)
                orientacion = random.choice(["H", "V"])

                colocado = self.colocar_barco(
                fila, columna, longitud, orientacion)

    def disparar(self, fila, columna, tablero_oponente):
        #Comprobamos si ya hemos disparado en esta casilla
        if self.disparos[fila][columna] != " ":
            
            return "already_shot"
        
        if tablero_oponente.tablero[fila][columna] == "B":
            self.disparos[fila][columna] = "X"
            tablero_oponente.tablero[fila][columna] = "X"
            
            return "hit"

        #Si no hay barco, es agua
            self.disparos[fila][columna] = "O"
            
            return "miss"