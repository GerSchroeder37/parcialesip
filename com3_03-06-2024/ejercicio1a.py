# Ejercicio 1: (2.5 puntos):
# a. Hacer una función que reciba una frase y la guarde en una lista donde cada palabra sea un elemento de la lista. Por ejemplo, 
# si recibe el artículo 5 del estatuto de la UNGS que dice: 
# "los recursos economicos del individuo o de la familia no deben ser el factor que determine la realizacion de las personas" 
# devuelve ["los", "recursos", "economicos", "del", "individuo", "o", "de", "la", "familia", "no", "deben", "ser", "el", 
# "factor", "que", "determine", "la", "realizacion", "de", "las", "personas"]
def lista_palabras(frase) :
    frase = frase + " "
    palabra = ""
    lista = []
    for char in frase :
        if char != " " :
            palabra += char
        else :
            lista.append(palabra)
            palabra = ""
    return lista