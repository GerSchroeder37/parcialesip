def doblete(numero) :
    suma_divisores = 0
    suma_digitos = 0
    for i in range(1,numero) :
        if numero % i == 0 :
            suma_divisores += i
    for num in str(numero) :
        suma_digitos += int(num)
    suma_digitos = suma_digitos * 2
    if suma_digitos == suma_divisores :
        return True
    return False