# Ejercicio 4 (2 puntos):
# Una empresa que se dedica al cobro de deudas posee un sistema con las siguientes funciones
# desarrolladas:
# apellido_deudores(): devuelve una lista con los apellidos de deudores a cobrar 
# deuda_deudores(): devuelve una lista con los montos adeudados de los deudores a cobrar
# mail_deudores(): devuelve una lista con los correos electrónicos de los deudores a cobrar
# Importante: se asume que las listas devueltas por las funciones, son correspondidas
# primer_aviso(apellido, deuda, email): envía un correo electrónico con el primer aviso de deuda 
# segundo_aviso(apellido, deuda, email): envia un correo electrónico con el segundo aviso de deuda
# se_envio_aviso(email): devuelve True o False si se ha enviado un correo de primer aviso al email
# Realizar el programa principal para:
# 1. Enviar un correo electrónico de primer aviso todos los deudores
# 2. Enviar un correo electrónico de segundo aviso a todos los deudores con deuda superior a 500.000$
# 3. Realizar un listado con los correos electrónicos de los deudores con deuda superior a 1.000.000$
# 4. Indicar apellido, deuda y correo electrónico del mayor deudor

# apellidos = apellido_deudores()
# deudas = deuda_deudores()
# mails = mail_deudores()
# mails_mayores_deudores = []
# mayor_deuda = -1
# indice_mayor_deudor = -1
# for i in range(len(apellidos)) :
#     if se_envio_aviso(mails[i]) == False :
#         primer_aviso(apellidos[i], deudas[i], mails[i])
#     else :
#         if deudas[i] > 500000 :
#             segundo_aviso(apellidos[i], deudas[i], mails[i])
#     if deudas[i] > 1000000 :
#         mails_mayores_deudores.append(mails[i])
#     if deudas[i] > mayor_deuda :
#         mayor_deuda = deudas[i]
#         indice_mayor_deudor = i
# print("El mayor deudor es",apellidos[indice_mayor_deudor],"la deuda es de",deudas[indice_mayor_deudor],"y su correo es",mails[indice_mayor_deudor])