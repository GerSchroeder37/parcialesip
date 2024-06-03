# Para un periódico digital, se desea implementar un sistema automatizado para clasificar noticias en tres niveles de importancia: baja, media y alta. Para ello, se proporcionan las siguientes funciones ya implementadas:
# 1. cadena_a_lista (cadena): Esta función recibe como parámetro una cadena de texto y devuelve la cantidad de palabras de la cadena.
# 2. sin_repetidas (lista): Esta función recibe como parámetro una lista de palabras y devuelve otra lista con las palabras, sin repeticiones.
# 3. cantidad_enlaces (noticia): Esta función recibe como parámetro una cadena de texto que representa el cuerpo de una noticia y devuelve la cantidad de enlaces incluidos en el cuerpo de la noticia.
# Nota: Los enlaces son relaciones entre palabras que permiten a los usuarios acceder a otros contenidos relacionados con la información que están leyendo. En el contexto de una noticia en linea, un enlace es una palabra o frase resaltada que, al hacer clic en ella, lleva al lector a otra página web o recurso en linea. Estos enlaces pueden proporcionar más detalles sobre el
# tema discutido en la noticia o dirigir a fuentes adicionales de información
# Utilizando estas funciones, se pide implementar la función:
# clasificar_noticia (titulo, noticia) que reciba como parámetro una cadena de texto que representa al titulo de la noticia y otra que corresponda al texto de la noticia. La función deberá determinar el nivel de importancia según los siguientes criterios:
# Será de baja importancia si la cantidad de palabras del cuerpo es hasta a 200 palabras, su titulo no supera las 10 palabras y la noticia puede tener hasta una palabra clave o un enlace.
# Se considerará de media importancia si la cantidad de palabras en el cuerpo de la noticia es hasta 200 palabras, posee por lo menos 1 palabra clave o 1 enlace en el cuerpo de la misma.
# Será considerada de alta importancia si supera las 200 palabras, contiene no menos de 3 palabras clave y
# por lo menos 1 enlace.
# La lista de "palabras clave" debe ser parte de la función a definir (Ejemplo: palabras_clave_alta_importancia ["urgente", "importante", "crisis", "emergencia"])
# La función clasificar_noticia (titulo, noticia) debe devolver un valor de acuerdo al nivel de importancia determinado: "Baja", "Media" o "Alta". Si no se cumple ninguno de los criterios anteriores, la función debe devolver "No se puede clasificar".
# Escribir el programa principal solicitando el ingreso de la noticia y su titulo, invocar a la función definida y mostrar una salida según el ejemplo.

def clasificar_noticia(titulo,noticia):
    lista_titulo = cadena_a_lista(titulo)
    lista_titulo = sin_repetidas(lista_titulo)
    lista_noticia = cadena_a_lista(noticia)
    lista_noticia = sin_repetidas(lista_noticia)
    nivel_importancia = "importancia baja"
    palabras_claves = ["urgente","importante","crisis"]
    enlaces = cantidad_enlaces(noticia)
    cantidad_palabras_clave = 0
    for palabra in lista_noticia:
        if palabra in palabras_clave:
            cantidad_palabras_clave+=1
    if len(lista_noticia) <= 200 and len(lista_titulo) <= 10 and (cantidad_palabras_clave <= 1 or enlaces <= 1):
        nivel_importancia = "importancia baja"
    elif len(lista_noticia) > 200 and cantidad_palabras_clave >= 3 and enlaces >= 1:
        nivel_importancia = "importancia alta"
    else:
        nivel_importancia = "no se puede clasificar"
    return nivel_importancia 
