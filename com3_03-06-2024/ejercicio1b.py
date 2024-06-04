# b. Hacer una función que reciba una frase y devuelva la palabra con mas vocales. En el ejemplo anterior debería devolver "realizacion".
from ejercicio1a import lista_palabras
def mas_vocales(frase) :
    lista = lista_palabras(frase)
    cant = 0
    cant_nueva = 0
    palabra_mas_vocales = ""
    for palabra in lista :
        cant_nueva = contar_vocales(palabra)
        if cant_nueva > cant :
            palabra_mas_vocales = palabra
            cant = cant_nueva
    return palabra_mas_vocales

def contar_vocales(palabra) : 
    cont = 0
    for char in palabra :
        if char=="a" or char=="e" or char=="i" or char=="o" or char=="u" :
            cont += 1
    return cont