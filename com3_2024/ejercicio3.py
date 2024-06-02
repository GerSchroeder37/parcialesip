# Ejercicio 3: 
# Se tienen las patentes de los vehículos y lo que a cada una les resta pagar de ese impuesto..
# Se pide programar una función patentesSinDeuda que reciba como parámetro, la lista de patentes y la lista de
# deudas y devuelva las patentes sin deuda.
# patentes ("AF23BCE", "AC123NE", "AD534FA, "AB871MN",...]
# deudas - [45725.87, 0, 42711.15, 0,...)
# print (patentesSinDeuda (patentes, deudas)) # deberá devolver ["AC123NE", "AB871MN",...]
def patentesSinDeuda(patentes,deuda):
    patentesSinDeuda = []
    contador = 0
    for patente in patentes:
        if deuda[contador] == 0:
            patentesSinDeuda.append(patente)
        contador += 1
    return patentesSinDeuda


patentes = ["AF238CE", "AC123NE", "AD534FA", "AB871MN"]
deudas = [45725.87, 0, 42711.15, 0]
ProgramaNuevo = patentesSinDeuda(patentes, deudas)
print("Las patentes sin deuda son:",ProgramaNuevo)