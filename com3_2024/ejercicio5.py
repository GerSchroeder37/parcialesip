# Ejercicio 5
# Hacer un programa que solicite al usuario la cantidad de términos que desea que calcule de la siguiente serie y muestre el valor final generado.
# Serie 3 - 9 + 27 81 + 243 - ... sigue

terminos = int(input("Ingrese la cantidad de terminos "))
contador= 1
signo = 1
i=-1
resultado = 0
while contador <= terminos :
    i= i*3*-signo
    resultado += i
    contador += 1
print(resultado)
