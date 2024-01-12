# Podemos decir que 2 listas son paralelas cuando hay una relacion entre
# las componentes de igual subindice (5 y 5, 2 y 2 elementos)

# Desarrollar un programa que permita cargar 5 nombres de personas y sus edades.
# Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas de mayor edad ( >= 18)

"""
nombres = []
edades = []

for x in range(5):
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    nombres.append(nombre)
    edades.append(edad)

for x in range(5):
    if edades[x] >= 18:
        print(nombres[x])



# PROBLEMAS PROPUESTOS
    
# Problema 1
# Crear y cargar dos listas con los nombres de 5 productos y sus respectivos precios en otra.
# Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado
        
productos = []
precios = []

for x in range(5):
    producto = input("Ingrese el producto: ")
    precio = float(input("Ingrese el precio del producto: "))

    productos.append(producto)
    precios.append(precio)

total = 0
for x in range(1,5):
    if precios[x] > precios[0]:
        total =  total + 1
        print(productos[x])



# Problema 2
# En un curso de 4 alumnos se registraron las notas de sus examentes y se deben procesar de acuerdo a los sigte:
# a) Ingresar nombre y nota de cada alumno(en listas separadas)
# b) Realizar un listado que muestre los nombres, notas y condicion del alumno(muy bueno nota >=8
# bueno nota >=4 insuficiente nota < 4)
# Imprimir cuantos alumnos tienen la leyendo muy bueno

alumnos = []
notas = []

for x in range(4):
    alumno = input("Cual es su nombre: ")
    nota = int(input("Cual es su nota: "))

    alumnos.append(alumno)
    notas.append(nota)

muy_bueno = 0
for x in range(4):
    print(alumnos[x])
    print(notas[x])
    if notas[x] >= 8:
        print("Muy Bueno")
        muy_bueno = muy_bueno + 1
    else:
        if notas[x] >= 4:
            print("Bueno")
        else:
            print("Insuficiente")

print("Alumnos con notas muy bueno:", muy_bueno)

"""

# Problema 3
# Realizar un programa que pida la carga de 2 listas con 4 elementos.
# Generar una tercera lista que surja de la suma de los elementos de la misma posicion de cada lista
# Mostrar la tercer lista

lista1 = []
lista2 = []
lista3 = []

for x in range(4):
    valor_lista1 = int(input("Ingrese el valor(lista1): "))
    valor_lista2 = int(input("Ingrese el valor(lista2): "))

    lista1.append(valor_lista1)
    lista2.append(valor_lista2)

    lista3.append(lista1[x] + lista2[x])

print(lista1)
print(lista2)
print(lista3)