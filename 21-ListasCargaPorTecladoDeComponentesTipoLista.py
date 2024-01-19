# En el concepto anterior vimos que facilmente podemos definir por asignacion una lista
# cuyas componentes sean tambien listas
# En Muchas ocaciones debemos crear una nueva lista ingresando
# los datos por teclado o por operaciones del mismo programa

# Problema 1
# Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene
# dos notas, almacenar las notas en una lista paralela.
# Cada componente de la lista paralela debe ser una lista con las dos notas.
# Imprimir luego cada nombre y sus dos notas.
"""
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

# Problema 2
# Se tiene que cargar la siguiente informacion:
# Nombre de 3 empleados
# Ingresos en concepto de sueldo, cobrado por cada empleado en los ultimos 3 meses
# Confeccionar el programa para

# a) Realizar la carga de los nombres de empleados y los 3 sueldos por cada empleado
# b) Generar una lista que contenga el ingreso acumulado en sueldos en los ultimos 3 meses cada uno
# c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los ultimos 3 meses
# d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado

# Deberia queda asi:
# nombres = ['juan', 'ana', 'luis']
# sueldos = [[500,510,500], [700,650,600], [250,250,250,]]
# totalSueldos = [1510, 1850, 750]

empleados = []
sueldos = []

for x in range(3):
    nombre = input("Ingrese su nombre: ")
    sueldo1 = int(input('Sueldo1: '))
    sueldo2 = int(input('Sueldo2: '))
    sueldo3 = int(input('Sueldo3: '))

    empleados.append(nombre)
    sueldos.append([sueldo1, sueldo2, sueldo3])

for x in range(3):
    print(empleados[x], sueldos[x])

totalSueldos = []
for x in range(len(sueldos)):
     suma = sueldos[x][0] + sueldos[x][1] + sueldos[x][2]
     totalSueldos.append(suma)
       
print(totalSueldos)


nombres = 0
mayor = totalSueldos[0]
for x in range(1,3):
     if totalSueldos[x] > mayor:
          mayor = totalSueldos[x]
          nombres = x

print(empleados[nombres])
         
    
"""
# Problema 3
# Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que 
# crearemos en la lista. El segundo valor indica la cantidad de elementos que tendra cada lista interna
# Mostrar la lista y la suma de todos sus elementos.
# ej 2 y 4
# lista = [[1,2,3,4], [1,2,3,4]]

tamanoLista = int(input('Cantidad de elementos de la lista: '))
tamanoSubLista = int(input('Cantidad de elementos de la sublista: '))

lista = []

for x in range(tamanoLista):
    lista.append([])
    for c in range(tamanoSubLista):
        valor = int(input('valor: '))
        lista[x].append(valor)
print(lista)