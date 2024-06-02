# programa principal del ejercicio 2
from ejercicio2parcial import *
cadena = input("Ingrese un texto ")
lista_palabras = separar_palabras(cadena)
lista_girada = girar_lista(lista_palabras)
print("Lista de palabras ",lista_palabras)
print("Lista girada",lista_girada)