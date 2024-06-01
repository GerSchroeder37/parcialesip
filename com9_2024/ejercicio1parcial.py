cadena="hola a todos"
encripcad=""
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
            
aleatorios=primosAleatorios(cadena)

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
        encripcad+=char
    

print(cadena)
print(encripcad)






    

















