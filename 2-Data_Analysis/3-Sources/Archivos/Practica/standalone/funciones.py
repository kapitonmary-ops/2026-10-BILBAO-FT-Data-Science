# Importamos las variables
from variables import ruta, categorias

# Importamos los módulos necesarios
import os
import shutil


# Definimos una función para crear las carpetas
def crear_carpetas():

    # Recorremos las categorías
    for categoria in categorias:

        # Definimos la ruta de la carpeta
        ruta_categoria = os.path.join(ruta, categoria)

        # Comprobamos si la carpeta existe
        if not os.path.exists(ruta_categoria):

            # Creamos la carpeta
            os.mkdir(ruta_categoria)



# Definimos una función para organizar los archivos
def organizar_archivos():

    # Recorremos los archivos de la carpeta
    for archivo in os.listdir(ruta):

        # Ignoramos los archivos del sistema macOS
        if archivo == '.DS_Store':
            continue

        # Comprobamos si el elemento es una carpeta
        if os.path.isdir(os.path.join(ruta, archivo)):
            continue

        # Obtenemos la extensión del archivo
        extension = os.path.splitext(archivo)[1].lower()

        # Buscamos la categoría correspondiente
        for categoria, extensiones in categorias.items():

            # Comprobamos si la extensión pertenece a la categoría
            if extension in extensiones:

                # Definimos la ruta de origen
                origen = os.path.join(ruta, archivo)

                # Definimos la ruta de destino
                destino = os.path.join(ruta, categoria)

                # Movemos el archivo
                shutil.move(origen, destino)

                # Terminamos la búsqueda
                break

        # Si el archivo no pertenece a ninguna categoría
        else:

            # Definimos la ruta de destino
            destino = os.path.join(ruta, 'Otros')

            # Movemos el archivo
            shutil.move(os.path.join(ruta, archivo), destino)
