# def clasificar_noticia(titulo,noticia):
#     lista_titulo = cadena_a_lista(titulo)
#     lista_titulo = sin_repetidas(lista_titulo)
#     lista_noticia = cadena_a_lista(noticia)
#     lista_noticia = sin_repetidas(lista_noticia)
#     nivel_importancia = "importancia baja"
#     palabras_claves = ["urgente","importante","crisis"]
#     enlaces = cantidad_enlaces(noticia)
#     cantidad_palabras_clave = 0
#     for palabra in lista_noticia:
#         if palabra in palabras_clave:
#             cantidad_palabras_clave+=1
#     if len(lista_noticia) <= 200 and len(lista_titulo) <= 10 and (cantidad_palabras_clave <= 1 or enlaces <= 1):
#         nivel_importancia = "importancia baja"
#     elif len(lista_noticia) > 200 and cantidad_palabras_clave >= 3 and enlaces >= 1:
#         nivel_importancia = "importancia alta"
#     else:
#         nivel_importancia = "no se puede clasificar"
#     return nivel_importancia 
