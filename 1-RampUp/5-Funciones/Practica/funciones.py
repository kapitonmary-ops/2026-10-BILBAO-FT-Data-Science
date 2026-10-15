<<<<<<< HEAD

import math


# Ejercicio 1: día de la semana
def dayweek(day):
    if day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 7:
        return "Sunday"
    else:
        return "error"


# Ejercicio 2: piramide invertida
def piramide(filas):
    for numero in range(filas, 0, -1):
        print()
        for otro_numero in range(numero, 0, -1):
            print(otro_numero, end=" ")


# Ejercicio 3: comparar dos números
def compare(arg1, arg2):
    if arg1 == arg2:
        return "son iguales"
    elif arg1 > arg2:
        return "el primero es mayor que el segundo"
    else:
        return "el segundo es mayor que el primero"


# Ejercicio 4: contar una letra
def quantity(text, letter):
    text = text.lower()
    letter = letter.lower()
    return text.count(letter)


# Ejercicio 5: contar todas las letras
def count_letters(word):
    my_dict = {}
    for letter in word:
        if letter in my_dict:
            my_dict[letter] += 1
        else:
            my_dict[letter] = 1
    return my_dict


# Ejercicio 6: añadir o eliminar elementos de una lista
def function(lista, comando, elemento=None):
    if comando == "add":
        lista.append(elemento)
    elif comando == "remove":
        lista.remove(elemento)
    return lista


# Ejercicio 7: unir palabras
def palabras(*words):
    return " ".join(words)


# Ejercicio 8: Fibonacci recursivo
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Ejercicio 9: áreas geométricas
def area_square(side):
    return side ** 2


def area_triangle(base, height):
    return base * height / 2


def area_circle(radius):
    return math.pi * radius ** 2
=======
import math

def ejercicio_1(dia):
    dias_semana = {1: "Lunes",
               2: "Martes",
               3: "Miércoles",
               4: "Jueves",
               5: "Viernes",
               6: "Sábado",
               7: "Domingo"}
    return dias_semana.get(dia, "Día erróneo")

def ejercicio_2(tamaño:int=5):
    lista_8 = list(range(int(tamaño),0,-1))
    while len(lista_8) > 0:
        print(*lista_8)
        lista_8.pop(0)

def ejercicio_3(num_1, num_2):
    if num_1 == num_2:
        out = "Son iguales"
    elif num_1 > num_2:
        out = "Primer número mayor que segundo"
    else:
        out = "Segundo número mayor que primero"
    return out

def limpieza_texto(texto, dict_vocales={'á':'a',
                                        'é':'e',
                                        'í':'i',
                                        'ó':'o',
                                        'ú':'u'}):
    texto = texto.lower()

    for clave in dict_vocales:
        texto = texto.replace(clave, dict_vocales[clave])
    return texto

def ejercicio_4(frase, letra):
    frase = limpieza_texto(frase)
    return frase.count(letra.lower())

def ejercicio_5(frase):

    dict_conteo = {}
    frase = limpieza_texto(frase)

    for caracter in frase:
        if caracter not in dict_conteo.keys() and caracter not in [" ", ","]:
            dict_conteo[caracter] = frase.count(caracter)

    return dict_conteo

def ejercicio_6(lista, comando, elemento=None):
    if comando == "add":
        lista.append(elemento)
    elif comando == "remove":
        try:
            lista.remove(elemento)
        except:
            print("El elemento no se encuentra en la lista")
    else:
        print("Comando no reconocido")
    return lista

def ejercicio_7(*args):
    return " ".join(args)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def cuadrado(l, n=1):
    return round(n * l ** 2, 2)

def triangulo(b, a):
    return round(b * a / 2, 2)

def circulo(r):
    return round(math.pi * r ** 2, 2)



if __name__ == "__main__":
    print(triangulo(3,7))
    print(circulo(10))
    print()
    
>>>>>>> upstream/main
