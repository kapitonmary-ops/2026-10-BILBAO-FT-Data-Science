
# Solicitamos una coordenada válida al usuario.
def pedir_coordenada():
    # Repetimos la solicitud hasta obtener una entrada válida.
    while True:
        try:
            coordenada = input("Enter a coordinate (0-9) or q  - to quit a Game: ")
            if coordenada == "q":   
                print ("Thanks for playing Battleship!")
                return None
            coordenada = int (coordenada)
        
        # Gestionamos el error si la entrada no es un número válido.
        except ValueError:
            print ("Please enter a number!")
            continue

        if coordenada <0 or coordenada > 9:
            print ("Invalid coordenate. Try again!") 
        else:
            return coordenada

 