
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
