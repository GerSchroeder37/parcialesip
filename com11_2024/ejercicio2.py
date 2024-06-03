# Ejercicio 2. 
# Desarrollar un algoritmo de encriptación de message El usuario ingresa una cadena, y el programa debe encriptarla siguiendo los siguimines pasos
# 1. Los espacios deben ser reemplazaden por Ejemplos
# "Merisaje a encristar "Mensajea encriptar "Otro mensaje "Otip mensaje
# 2 Lat.comonantes deben ser reemplazadas por la cantidad de con Ejemplos
# "Mensaje a encriptar 10101010101010101010" (la cadena tiene 10 consonantes
# mensaje "OGGn6666" (la cadena tiene l, consonantes).
# 3. Las vocales deben ser reemplazadas por números primos ardenados, de manera tal que la vocal número sea reemplazada por el primo nώπστα
# Es decir, si la cadena tienen vocales, la primera vocal debe ser reemplazada por el primer número pri (que os el númern 21, la segunda vocal debe ser reemplazada por el segundo número primo que es e númera 31, y así sucesivamente hasta llegar a la nésmo vocal, la cual debe ser reemplazada por el nesimo número primo
# "Memaje a encriptar" "10210103105*7*111010101310101710 (se reemplazan las vocales por los números premios 2-3-5-7-11-13-17)
# "Otro mensaje" "2663*65667611" (be reemplazan las vocales por los números prinids 2-3-5-7-111
# Sugerencig matizar la funcion genever_premos cantidad), que retome una lista con los primeros números primus

def es_primo(numero):
    resultado=True
    for i in range(2,numero):
        if numero %i==0:
            resultado=False
    return resultado

def generar_primos(cantidad):
    lista_primos=[]
    i=2
    while len(lista_primos)<cantidad:
        if es_primo(i):
            lista_primos.append(i)
        i+=1
    return lista_primos

mensaje=input("Ingrese el mensaje")
vocales="aeiou"
mensaje_encriptado=""
cantidad_vocales=0
cantidad_consonantes=0
for letra in mensaje:
    if letra in vocales:
        cantidad_vocales+=1
    else:
        cantidad_consonantes+=1
indice_primos=0
primos=generar_primos(cantidad_vocales)
for letra in mensaje:
    if letra==" ":
        mensaje_encriptado+="*"
    elif letra not in vocales:
        mensaje_encriptado+=str(cantidad_consonantes)
    elif letra in vocales:
        mensaje_encriptado+=str(primos[indice_primos])
        indice_primos+=1
print(mensaje_encriptado)

