"""
# 1 Estructura repetitiva for

for x in range(101):
    print(x)

 # 2 Realiza un programa que imprima en pantalla los numeros del 20 al 30   
    
for x in range(20,31):
    print(x)

# 3 Imprimir todos los numeros impares que hay entre 1 y 100
    
for x in range(1,100,2):
    print(x)

# 4 Desarrollar un programa que permita la carga de 10 numeros y nos muestre la
# suma y el promedio de los mismo.

suma = 0 
for x in range(1,11):
    numero = int(input("Ingrese un valor: "))
    suma = suma + numero

print("Suma de los valores:", suma)
promedio = suma / 10
print("El promedio es:",promedio)


# 5 Ingrese la nota de 10 alumnos e informar cuantos tiene notas mayor de 7 y menor de 7

mayor = 0
menor = 0
for a in range(1,11):
    nota = int(input("Ingre la nota: "))

    if nota >= 7:
        mayor = mayor + 1
    else:
        menor = menor + 1
print("Cantidad mayor7:", mayor)
print("Cantidad menor7:", menor)

# 6 Escribir un programa que lea 10 numeros y muestre cuantos valores ingresados
# fueron multiplos de 3 y 5

multiplo3 = 0
multiplo5 = 0

for numerosX in range(1,11):
    valor = int(input("ingrese un valor numerico: "))
    
    if valor % 3 == 0:
         multiplo3 = multiplo3 + 1    
    if valor % 5 == 0: 
        multiplo5 = multiplo5 + 1
   

print("Cantidad multiplos 3:", multiplo3)
print("Cantidad multiplos 5:", multiplo5)

# 7 Codificar un programa que lea n numeros y calcule la cantidad de valores >= a 1000

mayor1000 = 0
hasta = int(input("Ingrese el valor de numeros a registrar: "))
for rango in range(hasta):
    contar = int(input("Ingrese el valor: "))
    if contar >= 1000:
        mayor1000 = mayor1000 + 1

print("Cantidad de valores mayor a 1000:", mayor1000)

"""

# Problemas propuestos