# En el concepto anterior vimos que facilmente podemos definir por asignacion una lista
# cuyas componentes sean tambien listas
# En Muchas ocaciones debemos crear una nueva lista ingresando
# los datos por teclado o por operaciones del mismo programa

# Problema 1
# Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene
# dos notas, almacenar las notas en una lista paralela.
# Cada componente de la lista paralela debe ser una lista con las dos notas.
# Imprimir luego cada nombre y sus dos notas.

alumnos = []
notas = []

for n in range(3):
    alumno = input("Ingrese el nombre: ")
    alumnos.append(alumno)
    
    nota1 = int(input("Ingrese la nota: "))
    nota2 = int(input("Ingrese la nota: "))
    notas.append([nota1,nota2])
        
for x in range(len(alumnos)):
    print(alumnos[x], notas[x][0], notas[x][1])