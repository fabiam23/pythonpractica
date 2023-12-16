#Problema 1 , Realizar la carga de 2 numeros e imprimir  su suma y producto
num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor:"))
suma = num1 + num2
producto = num1 * num2
print("La suma de los dos valores es: ")
print(suma)
print("El producto de los dos valores es: ")
print(producto)


#problem 2, Cargar el precio de un producto y la cantidad a llevar. Mostrar cuanto se debe de pagar
precio = int(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad de productos a llevar: "))
importe = precio * cantidad
print(cantidad)

#PROBLEMAS PROPUESTOS
# 1- Realizar la carga de un lado de un cuadrado y mostara el perimetrol
lado = int(input("Ingrese un lado del cuadrado para calcular el perimetro: "))
perimetro = lado * 4
print("El perimetro del cuadrado es", perimetro)

# 2- Escribir un programa en el cual se ingresen 4 numeros, calcular la suma de los dos primeros y el producto del tercero y cuarto
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
num4 = int(input("Ingrese el cuarto numero: "))
suma = num1 + num2
producto = num3 * num4
print("La suma de los dos primeros numeros es: ", suma)
print("El producto de los dos ultimos numeros es ", producto)

# 3- Realizar un programa que lea cuatro valores numericos e informar su suma y promedio
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
num4 = int(input("Ingrese el cuarto numero: "))
suma = num1 + num2 + num3 + num4 
promedio = suma / 4
print("La suma de los numero es ", suma)
print("el promedio de los numeros es", promedio)


# 4- Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora
horaTrabajas = int(input("Ingrese la cantidad de horas trabajadas: "))
valorHoras = int(input("Indique el valor de las horas :"))
sueldo = horaTrabajas * valorHoras
print("El sueldo mensual de un operario es", sueldo)
