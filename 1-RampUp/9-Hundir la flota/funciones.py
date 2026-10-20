def pedir_coordenada():
    coordenada = int(input("Enter a coordinate (0-9): "))

    while coordenada < 0 or coordenada > 9:
        print("Invalid coordinate. Try again.")
        coordenada = int(input("Enter a coordinate (0-9): "))

    return coordenada