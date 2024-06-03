# Ejercicio 4
# Se lo convoca para colaborar en un proyecto sobre una app de una billetera virtual.
# Se dispone de las siguientes funciones ya programadas que debe utilizar para hacer lo que se le encarga.
# Las funciones que están involucradas con su parte de la app son:.
# damelmagen que recibe como parámetro una persona y devuelve una imagen
# dameMail que recibe como parámetro una persona y devuelve la dirección de mail de la persona ingresada
# verificacion que recibe como parámetros la imagen del DNI de una persona, se conecta con la base del RENAPER y
# devuelve True si el DNI pasa la verificación y False si no la pasa.
# enviarMail que recibe como parámetro una dirección de mail y un texto y envía el mail con ese texto a la dirección de mail indicada.
# Tiene que escribir una función comunicarResultado que recibe como parámetro una lista de personas y 
# debe comunicar a cada persona por mail el resultado de la verificación. La función debe hacer lo siguiente:
# Si el DNI pasa la verificación el texto del mail deberá decir: 
# DNI verificado!. En breve lo contactaremos, en caso contrario, 
# el texto del mail deberá decir: DNI no verificado!. Reinicie el trámite con una foto de mejor calidad.

 def comunicarResultado(personas) :
    for persona in personas :
         imagen = dameImagen(persona)
        mail = dameMail(persona)
         verificado = verificacion(imagen)
         texto = "DNI no verificado!. Reinicie el trámite con una foto de mejor calidad."
         if verificado :
             texto = "DNI verificado!. En breve lo contactaremos"
         enviarMail(mail,texto)
