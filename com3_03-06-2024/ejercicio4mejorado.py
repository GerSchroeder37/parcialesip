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
# Obtener el nombre de la universidad del usuario
universidad = input("Ingrese la universidad: ")

# Obtener la lista de estudiantes (DNIs) de la universidad
estudiantes = Estudiantes(universidad)

# Lista para almacenar los DNIs de los estudiantes que cumplen los requisitos para la beca
becas = []

# Iterar sobre cada estudiante
for dni in estudiantes:
    # Obtener las materias cursadas por el estudiante
    materias_cursadas = Cursadas(dni)
    
    # Variables para contar las materias con nota >= 9 y sumar todas las notas
    materias_con_nota_alta = 0
    suma_notas = 0
    
    # Iterar sobre cada materia cursada
    for materia in materias_cursadas:
        # Obtener la nota de la materia
        nota = NotaMateria(materia, dni)
        
        # Sumar la nota a la suma total
        suma_notas += nota
        
        # Contar si la nota es mayor o igual a 9
        if (nota >= 9):
            materias_con_nota_alta += 1
    
    # Calcular el promedio solo si el estudiante tiene materias cursadas
    if len(materias_cursadas) > 0:
        promedio = suma_notas / len(materias_cursadas)
        
        # Verificar si el estudiante cumple con los criterios para la beca
        if promedio >= 7 and materias_con_nota_alta >= 3:
            # Añadir el DNI del estudiante a la lista de becas
            becas.append(dni)

# Imprimir la lista de estudiantes que cumplen con los requisitos para la beca
print(becas)