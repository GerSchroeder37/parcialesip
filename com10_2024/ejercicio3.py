def sucesion(n) :
    num1=50
    num2=6
    num3=11
    num4=1
    signo=-1
    suma=0
    for i in range(1,n+1) :
        factorial = producto_factorial(num2)
        suma += (signo) * (num1*factorial)/(num3*num4)
        signo = signo * -1
        num1+=5
        num2+=2
        num3+=2
        num4 = num4 * 2
    return suma

def producto_factorial (n) :
    resultado = 1
    for i in range(1,n + 1) :
        resultado = resultado * i
    return resultado