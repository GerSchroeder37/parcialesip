# b) Desarrollar Un programa principal que utilice la función del punto anterior que ingresado un código de un libro determine 
# y muestre por pantalla su código, la cantidad de libros vendidos y el precio de ese libro
# c) Agregar al programa del punto b) los totales recaudados por libro
# EJEMPLO DE LO SOLICITADO: IMPORTANTE ES SOLO UN EJEMPLO DEBE FUNCIONAR CON CUALQUIER JUEGO DE LISTAS
# Codigo_Libros= [2345, 3567,1790, 7801] Cantidad_Vendidos = [10, 45, 12, 56] Precio_Libros= [8000, 10000, 15000, 5000]
# Si un usuario ingresa el Código 9034 el programa debe mostrar Libro no registrado
# Si un usuario ingresa el Código 1790 el programa debe mostrar:
# El código del libro: 1790 Cantidad Vendidos: 12 Precio del Libro: 15000 Total Recaudado por este libro 180.000.-
from ejercicio3a import DondeAparece
codigo = int(input("Ingrese el código del libro "))
Codigo_Libros= [2345, 3567,1790, 7801]
Cantidad_Vendidos = [10, 45, 12, 56]
Precio_Libros= [8000, 10000, 15000, 5000]
indice = DondeAparece(Codigo_Libros,codigo)
if indice == -1 :
    print("Libro no registrado")
else : 
    print("El código del libro:",Codigo_Libros[indice],"Cantidad Vendidos:",Cantidad_Vendidos[indice], "Precio del Libro:",Precio_Libros[indice])