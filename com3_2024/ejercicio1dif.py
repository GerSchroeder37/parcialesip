def anagrama(palabra1,palabra2):
    if len(palabra1)!=len(palabra2):  #chequeo que tenga misma cantidad de letras
        return False
    cantlet=0
    for char in palabra1:
        if char in palabra2:  #chequeo que cada letra de cierta palabra este en la otra
            cantlet+=len(char)  #agrego la cantidad de letras que estan en la palabra distinta de la misma
    if cantlet==len(palabra2) and palabra1!=palabra2:
        return "son anagramas"
    else:
        return "no son anagramas"




#programa principal
palabra1=input("Ingrese primer palabra")
palabra2=input("Ingrese segunda palabra")
print(anagrama(palabra1,palabra2))

