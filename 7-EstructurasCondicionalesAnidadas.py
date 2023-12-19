#Problema EJERCICIO
#Confecionar un programa que pida por teclado 3 notas de un alumno, calcule el promedio e imprima alguno de estos mensajes
#si el promedio es >= 7 mostrar promocionado
#si el promedio es >= 4 mostrar regular
#si el promedio es < 4 mostrar reprobado

nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 7:
    print("Promocionado")
elif promedio >= 4:
          print("Regular")
else:
    print("Reprobado")

#Problemas propuestos

#7-1 Se cargan por teclado 3 numero distintos. Mostrar el mayor de ellos
num1 = int(input("Ingrese el primer valor de (3): "))
num2 = int(input("Ingrese el segundo valor de (3): "))
num3 = int(input("Ingrese el tercer valor de (3): "))

if num1 > num2:
      if num1 > num3:
            print("Num1 es mayor: ",num1)
      else:
            print("Num3 es mayor: ", num3)
else:
      if num2 > num3:
            print("Num2 es mayor: ", num2)
      else:
            print("Num3 es mayor: ", num3)
    
#7-2 se tomara el valor de num1 para resolver el ejercicio
#Mostrar una leyenda si el numero es positivo, negativo o nulo
if num1 > 0:
      print("Positivo: ", num1)
else:
      if num1 == 0:
            print("Nulo: ", num1)
      else:
            print("Negativo:", num1)

#7-3 Mostrar la cantidad de cifras que tiene un numero, 1,2 o 3. Mostrar un mensaje de error si tiene mas
cifras = int(input("Ingrese un valor para ver la cantidad de cifras: "))

if cifras < 10:
      print("Tiene 1 cifra", cifras)
else:
      if cifras < 100:
            print("Tiene 2 cifras", cifras)
      else:
            if cifras < 1000:
                  print("Tiene 3 cifras", cifras)
            else:
                  print("Error")

#7-4 Test de capacitacion. Mostrar porcierto de un total de preguntas vs respuestas correctas
#maximo >= 90
#medio >= 75
#regular >= 50
#fuera de nivel < 50

cantidadPreguntas = int(input("Cantidad de preguntas realizadas: "))
cantidadCorrectas = int(input("Cantidad de preguntas acertadas: "))

porciertoPreguntas = (cantidadCorrectas / cantidadPreguntas) * 100
if porciertoPreguntas >= 90:
      print("Maximo:",porciertoPreguntas)
else:
      if porciertoPreguntas >= 75:
            print("Medio:", porciertoPreguntas)
      else:
            if porciertoPreguntas >= 50:
                  print("Regular:", porciertoPreguntas)
            else:
                  print("Fuera de nivel:", porciertoPreguntas)