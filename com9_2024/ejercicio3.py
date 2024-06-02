# Ejercicio 3:
# Realizar un programa principal y funciones, si considera conveniente, 
# para calcular la suma de los primeros n términos de la siguiente sucesión (la cantidad de términos se ingresa por teclado):
# S= 17*4! / 25*1 - 19*6! / 30*3 + 21*8! / 35*9 - 23*10! / 40*27 + ...
def sucesion(n) :
    num1= 17
    num2= 4
    num3= 25
    num4= 1
    signo = 1
    resultado = 0
    for i in range(1,n+1):
        calculo_factorial = factorial(num2)
        resultado += (signo*((num1*calculo_factorial)/(num3*num4)))
        signo *= -1
        num1 += 2
        num2 += 2
        num3 += 5
        num4 *= 3
    return resultado


def factorial(num):
    resultado = 1
    for i in range(1,num+1) :
        resultado *= i
    return resultado