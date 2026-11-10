# Importamos el módulo os
import os

# Definimos la ruta de la carpeta
ruta = os.path.expanduser("~/Desktop/Bridge(copy)")

# Definimos las categorías de archivos
categorias = {
    'Documentos': ['.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx'],
    'Imagenes': ['.jpg', '.jpeg', '.png', '.svg', '.gif'],
    'Software': ['.exe', '.py', '.ipynb'],
    'Otros': []
}