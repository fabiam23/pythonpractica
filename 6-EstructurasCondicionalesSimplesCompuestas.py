#Problema 1
#Condicional Simple
#Ingresar el sueldo de una persona, si supera los $3,000 mostrar un mensaje en pantalla
#indicando que debe abonar impuestos

sueldo = int(input("Ingrese el sueldo: "))
if sueldo > 3000:
    print("Esta persona debe abonar impuestos")

#Condicional Compuesta
#Realizar un programa que solicite ingresar dos numeros distintos y muestre el mayor de ellos

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
if num1 > num2:
    print("Numero 1 es mayor")
else:
    print("Numero 2 es mayor")

#Problemas propuestos
#2-1 Realizar un programa que solicite la carga de 2 numeros, si el primero es mayor que el segundo
#mostra la suma y la diferencia en caso contrario mostrar el producto y la division
valor1 = int(input("Ingrese un valor: "))
valor2 = int(input("Ingrese un valor: "))
if valor1 > valor2:
    suma = valor1 + valor2
    resta = valor1 - valor2
    print("La suma es:", suma)
    print("La Resta es:", resta)
else:
    producto = valor2 * valor1
    cociente = valor2 / valor1
    print("El producto es:", producto)
    print("El cociente es:", cociente)

#2-2 Se ingresan 3 notas de un alumno, si el promedio es >= 7 mostra promocionado
nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3
print("El promedio es:", promedio)

#Se ingresa por teclado un numero positivo de 1 o 2 digitos, indicar cuantos digitos tiene
digito = int(input("Ingrese un valor de 1 o 2 digitos: "))
if digito < 10:
    print("Tiene un digito", digito)
else:
    print("Tiene 2 digitos", digito)