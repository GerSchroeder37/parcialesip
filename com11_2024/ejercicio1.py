# Ejercicio 1:
# Hacer un programa, con las funciones que correspondan para que dado un número entero n 
# indique la cantidad de términos necesarios para que la serie supere al número n. 
# En esta serie el numerador y 
# la base del denominador es el mismo valor numérico par (el rango de los valores posibles se encuentra entre 2 y 2000) 
# у el valor numérico del exponente del denominador es la mitad del número obtenido al azar anteriormente:
# Ejemplo: 2/2^1 + 12/12^6 + 8/8^4 + 4/4^2 + 12/12^6 + 16/16^6 + 4/4^4 + …
import random
def es_par(n):
    resultado = False
    if n% 2  == 0 :
        resultado = True
    return resultado
serie = 0
n=int(input("Ingrese un numero: "))
cantidad_terminos = 0
while serie < n :
    numero = 0
    seguir = True
    while seguir:
        numero= random.randint(2,2000)
        if es_par(numero):
            seguir=False
        fraccion= numero/numero**(numero/2)
        serie +=fraccion
        cantidad_terminos += 1
print(cantidad_terminos)