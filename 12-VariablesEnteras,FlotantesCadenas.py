# Iniciar variables por asignacion
# Se define la variable entera
cantidad = 20
# Se define la variable flotante
altura = 1.92
# Definicion de una cadena de caracteres
dia = "lunes"
dias = 'mates'
# Carga para una cadena de caracteres
"""
nombre = input("Ingrese su nombre: ")

# Problema 1:
# Realizar la carga por teclado del nombre, edad y altura de dos personas
# Mostrar por pantalla el nombre de la persona con mayor altura

nombre1 = input("Nombre persona1: ")
edad1 = int(input("Edad persona1: "))
altura1 = float(input("Altura persona1: "))
nombre2 = input("Nombre persona2: ")
edad2 = int(input("Edad persona2: "))
altura2 = float(input("Altura persona2: "))

if altura1 > altura2:
    print(nombre1)
else:
    print(nombre2)


# Problema 2
# Realizar la carga de dos nombres por teclado. Mostrar cual de los 2 es mayor alfabeticamente
# hablando o si son iguales.

nombre1 = input("ingrese su nombre: ")
nombre2 = input("Ingrese su nombre: ")

if nombre1 > nombre2:
    print("nombre1 es mas grando:", nombre1)
else:
    if nombre2 > nombre1:
        print("nombre2 es mas grande:", nombre2)
    else:
        print("son iguales")

# Mientras mas lejos del principio este la letra de mayor tamano sera f > a
# Las Letras en mayusculas ZDFFE son menores que las minisculas zdfff
        

# Problema 3
# Realizar la carga de enteros por teclado. Preguntar despues que ingresa el valor si desea
# cargar otro valor, indicado por la cadena 'si' o 'no'

opcion = 'si'
suma = 0

while opcion == 'si':
    
    valor1 = int(input("Ingrese un valor: "))
    suma = suma + valor1

    opcion = input("Desea agregar otro valor: ")

print(suma)

"""
# PROBLEMAS PROPUESTOS

# Realizar la carga de dos nombres de personas distintos
# Mostrar por pantalla, ordenados en forma alfabetica

nombre1 = input("Primer nombre: ")
nombre2 = input("Segundo nombre: ")
if nombre1 < nombre2:
    print("nombres ordenados alfabeticamente")
    print(nombre1)
    print(nombre2)
else:
    print("nombres ordenados alfabeticamente")
    print(nombre2)
    print(nombre1)