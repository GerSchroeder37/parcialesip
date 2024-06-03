# Ejercicio 1 (3 puntos):
# Se nos solicita desarrollar el programa principal y las funciones necesarias para implementar un algoritmo de encriptación de mensajes. El usuario ingresa una cadena, y el programa debe encriptarla siguiendo los siguientes pasos:
# 1. Los espacios deben ser reemplazados por "#". Ejemplo:
# "Mensaje para encriptar" "Mensaje#para#encriptar".
# 2. Las vocales deben ser reemplazadas por la cantidad de vocales. Ejemplo:
# "Mensaje para encriptar" "M8ns8j8#p8r8#8ncr8pt8r" (la cadena tiene 8 vocales).
# 3. Las consonantes deben ser reemplazadas por números primos aleatorios entre 0 y 100. Ejemplo:
# "Mensaje para encriptar" "38278118#58138#8115382785" (se reemplazan las consonantes por los números primos aleatorios 3-2-7-11-5-13-11-5-3-2-7-5).
# Sugerencia: realizar la función obtener_primo_aleatorio().

cadena="hola a todos"
encripcad="" #cadea nueva encriptada
vocales="aeiou"
cantvocales=0
import random

def primosAleatorios(cad):
    encripcad=""
    for char in cadena:
        if char not in vocales and char!=" ":
            nroaleatorio=random.randrange(0,100)
            char=str(nroaleatorio)
            encripcad+=char
        else:
            encripcad+=char
    return encripcad
            
aleatorios=primosAleatorios(cadena) #"Hola a todos"

for char in aleatorios:
    if char in vocales:
        cantvocales+=1
    


for char in aleatorios: 
    if char in " ":
        encripcad+="#" #tapo los espacios por # 
    if char in vocales:
        char=str(cantvocales)
        encripcad+=char
    else:
        if char!=" ":
            encripcad+=char
    

print(cadena)
print(encripcad)






    

















