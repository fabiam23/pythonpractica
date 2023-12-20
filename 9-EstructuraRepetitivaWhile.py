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