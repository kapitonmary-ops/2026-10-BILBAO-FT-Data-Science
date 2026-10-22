# Importamos el módulo para generar valores aleatorios.
import random

# Importamos el tamaño del tablero y la flota desde variables.py.
from variables import TAMANO_TABLERO, FLOTA

# Definimos la clase que representa el tablero de cada jugador.
class Tablero:

    # Inicializamos el tablero del jugador.
    def __init__(self, player_id):
        # Guardamos el identificador del jugador.   
        self.player_id = player_id
        # Creamos el tablero vacío de 10 filas y 10 columnas.   
        self.tablero = [[" " for j in range(TAMANO_TABLERO)] for i in range(TAMANO_TABLERO)]
        # Creamos una matriz vacía para registrar los disparos.
        self.disparos = [[" " for j in range(TAMANO_TABLERO)] for i in range(TAMANO_TABLERO)]
        # Creamos una copia de la flota para cada jugador.
        self.flota = FLOTA.copy()

    
    # Colocamos un barco en una posición y orientación determinadas.
    def colocar_barco(self, fila, columna, longitud, orientacion):
        # Inicializamos los cambios de fila y columna.     
        cambio_fila = 0
        cambio_columna = 0

        # Si la orientación es horizontal, avanzamos por las columnas.        
        if orientacion == "H":
            cambio_columna = 1
        # Si la orientación es vertical, avanzamos por las filas.            
        elif orientacion == "V":
            cambio_fila = 1
        # Si la orientación no es válida, rechazamos la posición.            
        else: 
            return False
                
        # Comprobamos todas las casillas del barco antes de colocarlo.
        for i in range(longitud):
            nueva_fila = fila + i * cambio_fila
            nueva_columna = columna + i * cambio_columna
            
            # Comprobamos que la casilla esté dentro de los límites del tablero.
            if (nueva_fila < 0 or nueva_fila >= TAMANO_TABLERO or nueva_columna < 0 
                    or nueva_columna >= TAMANO_TABLERO):
                return False

            # Comprobamos que la casilla está libre.
            if self.tablero[nueva_fila][nueva_columna] != " ":
                return False
            
        
        # Si todas las casillas están libres, colocamos el barco
        for i in range(longitud):
            nueva_fila = fila + i * cambio_fila
            nueva_columna = columna + i * cambio_columna
            self.tablero[nueva_fila][nueva_columna] = "🚢"
        # Indicamos que el barco se ha colocado correctamente.
        return True 
    
    # Colocamos todos los barcos de la flota en posiciones aleatorias.  
    def colocar_flota_aleatoria(self):
        # Recorremos todos los barcos de la flota.
        for nombre, longitud in self.flota.items(): #перебирає кораблі у словнику Flota
            # Indicamos que el barco todavía no está colocado.
            colocado = False

            # Repetimos los intentos hasta colocar el barco correctamente.  
            while not colocado: 

                # Elegimos una fila, una columna y una orientación aleatorias.
                fila = random.randint(0, TAMANO_TABLERO - 1)
                columna = random.randint(0, TAMANO_TABLERO - 1)
                orientacion = random.choice(["H", "V"])
                # Intentamos colocar el barco y guardamos el resultado.
                colocado = self.colocar_barco(fila, columna, longitud, orientacion)



    # Registramos los resultados de nuestros disparos y consultamos el tablero del oponente.
    #self.disparos зберігає результати пострілів поточного гравця, а tablero_oponente.tablero — стан поля суперника
    def disparar(self, fila, columna, tablero_oponente):
        # Comprobamos si ya hemos disparado en esta casilla.
        if self.disparos[fila][columna] != " ":
            return "already_shot"

        # Comprobamos si hay un barco en la casilla elegida.
        if tablero_oponente.tablero[fila][columna] == "🚢":
            # Registramos el impacto en nuestro historial de disparos.
            self.disparos[fila][columna] = "X"
            # Marcamos el impacto en el tablero del oponente.
            tablero_oponente.tablero[fila][columna] = "X"
            return "hit"

        # Si no hay ningún barco, registramos agua.
        else:
            self.disparos[fila][columna] = "O"
            print("¡Agua!")
            return "miss"