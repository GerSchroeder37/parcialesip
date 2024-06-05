# Ejercicio 2 (2.5 puntos):
# Hacer un programa que calcule la siguiente serie:
# 10 + 2/3 - 4/5^3 + 6/7^5 - 8/9^7 + 10/11^9 - 12/13^11 ...
n = int(input("Ingrese un número de terminos mayor a 0 "))
resultado = 10
num1 = 2
num2= 3
potencia = 1
signo = 1

if n == 1 :
    print(resultado)

if n > 1 :
    for i in range(1,n) :
        resultado += (signo)*((num1)/(num2**potencia))
        num1 += 2
        num2 += 2
        potencia += 2
        signo = signo * -1
    print(resultado)