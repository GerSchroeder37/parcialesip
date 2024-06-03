

nombre = input("ingrese el nombre")
apellido = input("ingrese su apellido")
dni=input("ingrese su dni sin puntos ni comas")

cont=0
consonante="" 
for letra in nombre:
    if letra != "a" and letra !=  "e" and letra !=  "i" and letra != "o" and letra != "u" and cont<2:
        cont+=1
        consonante+=letra.upper()


vocal=""
for letra in apellido:
    if letra == "a" or letra ==  "e" or letra ==  "i" or letra == "o" or letra == "u":
        vocal=letra.lower()


suma=0
for numero in dni:
    suma+=int(numero)


codigo=consonante+vocal+str(suma)
print(codigo)