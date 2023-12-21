#Imprimir los numeros del 1 al 100
x = 2
while x <= 100:
    print(x)
    x = x + 2

# Codificar un programa que muestre los numeros del 1 hasta el valor indicado
final = int(input("Ingrese el ultimo valor hasta donde desea contar: "))

x = 1
while x <= final:
    print(x)
    x = x + 1
 
 # Codificar un programa que permita 10 numeros y muestre la suma y el promedio

n = 1
suma = 0

while n <= 10:
    valor = int(input("Ingrese un valor: "))
    n = n + 1
    suma = suma + valor

print("La suma es:",suma)
promedio = suma / 10
print("El promedio es:", promedio)

# Una planta fabrica perfiles de hierro y posee n # de piezas
# Confeccionar un programa que pida ingresar n # de piezas y luego
# ingrese la longitud, sabiendo que la longitud del perfil esta entre
# 1.20 y 1.30. imprimir la cantidad de piezas aptas

piezas = int(input("Ingrese la cantidad de piezas: "))
p = 0
piezasAptas = 0

while p < piezas:
    tamanoPieza = float(input("Ingrese el tamano de la pieza: "))

    if tamanoPieza >= 1.20 and tamanoPieza <= 1.30:
        piezasAptas = piezasAptas + 1
    p = p + 1
print("Cantidad de piezas buenas",piezasAptas, "de",piezas,"piezas")

#PROBLEMAS PROPUESTOS

# 9-1 Escribir un programa que cargue 10 notas de alumnos e informe cuantos tienen
# notas mayores a igual a 7 y cuantos menores

acumulador = 1
mayor = 0
menor = 0

while acumulador <= 10:
    notas = int(input("Ingrese la nota: "))

    if notas >= 7:
        mayor = mayor + 1
    else:
        menor = menor + 1
    
    acumulador = acumulador +1

print(" Mayor de 7:",mayor)
print("Menor de 7:", menor)

# 9-2 Se ingresan un conjunto de n alturas. Mostrar la altura promedio

acumulador1 = 1
totalAlturas = 0
cantidadAltura = int(input("Cuantas estaturas desea registrar: "))

while acumulador1 <= cantidadAltura:
    altura = float(input("Ingrese la altura: "))
    totalAlturas = totalAlturas + altura
    acumulador1 = acumulador1 + 1

promedio = totalAlturas / cantidadAltura
print("Total altura:", totalAlturas)
print("Altura promedio:", promedio)

# 9-3 En una empresa trabajan n empleados con sueldos entre 100 y 500, realizar 
# un programa que lea los sueldos de cada empleado y mostrar cuantos cobran entre
# 100 y 300 y cuantos mas de 300. Y mostrar cuanto gasta la empresa en total

acumulador2 = 1
totalsueldo = 0
sueldo100_300 = 0
sueldoMayor = 0

cantidadEmpleados = int(input("Cuantos empleados hay en la empresa: "))
while acumulador2 <= cantidadEmpleados:
    sueldo = int(input("Ingrese el sueldo: "))
    totalsueldo = totalsueldo + sueldo

    if sueldo >= 100 and sueldo <= 300:
        sueldo100_300 = sueldo100_300 + 1
    else: 
        if sueldo > 300:
            sueldoMayor = sueldoMayor + 1
    acumulador2 = acumulador2 + 1

print("Total en sueldo:", totalsueldo)
print("Sueldo entre 100 y 300:", sueldo100_300)
print("Sueldo mayor 300", sueldoMayor)

# 9-4