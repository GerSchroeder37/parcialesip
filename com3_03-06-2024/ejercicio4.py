# Ejercicio 4: (2.5 puntos):
# La Universidad desea asignar becas a aquellos estudiantes que han demostrado un rendimiento académico sobresaliente. 
# Para ello, la secretaría académica requiere un programa que identifique a los estudiantes que
# cumplan con los siguientes criterios:
# Haber aprobado al menos 3 materias con una nota mayor o igual a 9.
# Tener un promedio general de notas mayor o igual a 7.
# El área de computación ya cuenta con las siguientes funciones que te serán útiles para resolver este problema o sea no 
# debes desarrollar las funciones que se indican a continuación, solo utilizarlas con los parámetros que se
# encuentran:
# Estudiantes (universidad): Devuelve una lista de los DNIs de los estudiantes de esa Universidad.
# Cursadas (dni): Devuelve una lista con todas las materias cursadas por ese estudiante. 
# NotaMateria (materia, dni): Devuelve la nota obtenida por un estudiante en una materia específica.
# Tu tarea es escribir un programa que utilice estas funciones y devuelva una lista con los DNIs de los estudiantes 
# que cumplen con los criterios para recibir una beca.
universidad = input("Ingrese la universidad ")
est = Estudiantes(universidad)
becas = []
for i in range(len(est)):
    notas = []
    cursadas = Cursadas(est[i])
    cont_nota = 0
    suma = 0
    for materia in cursadas :
        nota= NotaMateria(materia,est[i])
        notas.append(nota)
        suma += nota
        if nota >= 9 :
            cont_nota += 1
    promedio = suma/len(notas)
    if promedio >= 7 and cont_nota >= 3 :
        becas.append(est[i])
print(becas)