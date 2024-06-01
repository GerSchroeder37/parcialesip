# Ejercicio 4
# Una empresa que se dedica al cobro de deudas posee un sistema con las siguientes funciones desarrolladas:
# apellido_deudores(): devuelve una lista con los apellidos de deudores a cobrar.
# deuda_deudores(): devuelve una lista con los montos adeudados de los deudores a cobrar.
# mail_deudores(): devuelve una lista con los correos electrónicos de los deudores a cobrar.
# Importante: se asume que las listas devueltas por las funciones, son correspondidas.
# primer_aviso(apellido, deuda, email): envía un correo electrónico con el primer aviso de deuda.
# segundo_aviso (apellido, deuda, email): envía un correo electrónico con el segundo aviso de deuda.
# se_envio_aviso (email): devuelve True o False si se ha enviado un correo de primer aviso al email.
# Realizar el programa principal para:
# 1. Enviar un correo electrónico de primer aviso a todos los deudores que no tuviesen primer aviso.
# 2. Enviar un correo electrónico de segundo aviso a todos los deudores con deuda superior a 350.000$.
# 3. Realizar una lista con los correos electrónicos de los deudores con deuda superior a 700.000$.
# 4. Mostrar apellido, deuda y correo electrónico del mayor deudor.

apellidos = apellido_deudores()
deudas = deuda_deudores()
mails = mail_deudores()
lista_mayores_deudores = []
mayor_deudor = []
for i in range(len(apellidos)) :
    if(se_envio_aviso(mails[i]) == False) :
        primer_aviso(apellidos[i],deudas[i],mails[i])
    else :
        if(deudas[i] > 350000) :
            segundo_aviso(apellidos[i],deudas[i],mails[i])
    if(deudas[i] > 700000) :
        lista_mayores_deudores.append(mails[i])
indice_mail = -1
mayor_deuda = 0

for i in range(len(mails)) :
    for mail in lista_mayores_deudores :
        if mails[i] == mail and deudas[i] > mayor_deuda :
            indice_mail = i
            mayor_deuda = deudas[i]
print("El mayor deudor es:",apellidos[indice_mail],"con una deuda de:",deudas[indice_mail],"y su correo es",mails[indice_mail])