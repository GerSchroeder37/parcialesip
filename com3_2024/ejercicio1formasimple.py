# Ejercicio 1
# Escribir una función llamada anagrama, que reciba 2 palabras y retorne True si las palabras son anagrama y False si no lo son. Ojo: Si las dos palabras fueran iguales, no son anagrama.

# Ejemplo de anagramas:

# peinar y plema
# cuna y nuca
# los y sol
# Ejemplo de No anagramas:

# peinar y peinar
# carne y acres
# arca y cata
def anagrama(palabra1,palabra2) :
    resultado= True
    if palabra1 == palabra2:
        return False
    
    if len(palabra1) != len(palabra2):
        return False
    for char in palabra1 :
        if char not in palabra2 :
            resultado=False

    return resultado

palabra1=input("ingrese una palabra:")
palabra2=input("ingrese otra palabra:")
esanagrama=anagrama(palabra1,palabra2)
print(esanagrama)