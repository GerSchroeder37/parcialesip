# Ejercicio 3: (2.5 puntos):
# La librería de la Universidad guarda su información en 3 listas que se corresponden:
# La primera Lista almacena el código del libro, el mismo no se repite. La segunda Lista guarda la cantidad vendida. 
# La tercera Lista almacena el precio de cada libro.
# Se solicita:
# a) Desarrollar la función DondeAparece con 2 parámetros: Una lista de enteros y un entero 
# La función debe retornar la posición de ese entero en la lista en caso de que ese entero se encuentre o -1 si no se encuentra

def DondeAparece(lista,n) :
    indice = -1
    for i in range(len(lista)) :
        if lista[i] == n :
            indice = i
    return indice