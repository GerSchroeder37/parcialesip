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
def anagrama(palabra1, palabra2):
    if palabra1 == palabra2:
        return False
    
    if len(palabra1) != len(palabra2):
        return False
    contador=0
    contador1=0
    for char1 in palabra1:
        contador+=aparece(char1,palabra2)
    for char1 in palabra2:
        contador1+=aparece(char1,palabra1)
    if contador==len(palabra1) and contador1==len(palabra1):
        return True
    else:
        return False       
def aparece(caracter,palabra):
    for char2 in palabra:
        if caracter==char2:
            return 1
    return 0
    
palabra1=input("ingrese una palabra:")
palabra2=input("ingrese otra palabra:")
esanagrama=anagrama(palabra1,palabra2)
print(esanagrama)