# Ejercicio 2
# Escribir una función paresEnLaInterseccion que reciba como parámetro dos listas de números y devuelva la cantidad de números pares en la intersección de ambas listas.
# Por ejemplo:
# Si una lista fuera: [24, 125, 32, 10, 56, 100, 90, 17]
# y la otra lista fuera: [199, 254, 17, 24, 32, 5, 12, 56, 145]
# la intersección de ambas sería: [24, 17, 32, 56]
# Por ende, la función paresEnLaInterseccion debe devolver 3, ya que hay 3 números pares en la intersección.

def paresEnLaInterseccion(lista1, lista2):
    interseccion = []

    for i in lista1:
        if i in lista2:
            interseccion.append(i)
   ## print(interseccion)
    contador = 0
    for i in interseccion:
        if i % 2 == 0:
            contador += 1
    return contador
lista1 = [24, 125, 32, 10, 56, 100, 90, 17]
lista2 = [199, 254, 17, 24, 32, 5, 12, 56, 145]
resultado = paresEnLaInterseccion(lista1, lista2)
print(resultado)  