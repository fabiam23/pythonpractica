#Problema
#Confeccionar un programa que lea 3 numeros distintos y nos muestre el mayor

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))

if num1 > num2 and num1 > num3:
    print("El primero es mayor")
else:
    if num2 > num3:
        print("El segundo es mayor")
    else:
        print("El tercero es mayor")

#Cargar una fecha (dia, mes, ano). Mostrar si corresponde al primer trimestre del ano(enero, febrero, marzo)
#Cargar la fecha solo con numeros dia 2, mes 3, ano 2020
dia = int(input("Ingrese un dia del mes: "))
mes = int(input("Ingrese el dia del mes: "))
ano = int(input("Ingrese el ano: "))

if mes == 1 or mes == 2 or mes == 3:
    print("Pertecene al primer trimestre")
    print("Dia",dia, " mes",mes, " ano",ano)

#problemas 
#8-1 Realizar un programa que pida cargar una fecha y verificar si corresponde a navidad
#se utilizan las variables del ejercicio anterior
if dia == 25 and mes == 12:
    print("Es Navidad, dia",dia, " mes",mes, " ano",ano )

#8-2 Se ingresan 3 numeros, si todos son menores a 10 imprimir la leyenda, todos los numeros son menores que 10
#Se utilizan las variables del primer problema num1 num2, num3
if num1 < 10 and num2 < 10 and num3 < 10:
    print("Todos los numeros son menor que 10")

#8-3 Se ingresan 3 numero si al menos 1 es menor a 10, imprimir en pantalla algun numero es menor a 10
#Se utilizan las variables del primer problema num1 num2, num3
if num1 < 10 or num2 < 10 or num3 < 10:
    print("Algun numero es menor a 10")

#8-4 Se ingresan 3 valores, si todos son iguales, se imprime la suma del primero con el segundo y el resultado se multiplica por el tercero
#Se utilizan las variables del primer problema num1 num2, num3

if num1 == num2 and num2 == num3:
    resultado = (num1 + num2) * num3
    print("El resultado es:", resultado)

#8-5 Escribir un programa que pida dos valores e indique el cuadrante al que pertenece
coordenadaX = int(input("Indique la primer coordenada: "))
coordenadaY = int(input("Indique la segunda coordenada: "))

if (coordenadaX < 0 and coordenadaY > 0):
    print("Pertenece al primer cuadrante")
else:
    if (coordenadaX > 0 and coordenadaY > 0):
        print("Pertenece al segundo cuadrante")
    else:
        if (coordenadaX < 0 and coordenadaY < 0):
            print("Pertenece al tercer cuadrante")
        else:
            print("Pertenece al cuarto cuadrante")

#8-6 Se conocen los datos de un operario, su sueldo y anos
# Indicar si el sueldo es menor a 500 y su antiguedad es igual o superior a 10, un aumento del 20%
# Si su sueldo es inferior a 500 pero su antiguedad es menor a 10, un aumento de 5%
# Si su sueldo es mayor a 500 mostrar el sueldo en pantalla
            
sueldo = int(input("Ingrese su sueldo: "))
anos = int(input("Ingrese los anos en la empresa: "))

if sueldo < 500 and anos >= 10:
    aumento = sueldo * 0.20
    print("aumento:",aumento)
    print("nuevo sueldo,", sueldo + aumento)
else:
    if sueldo < 500 and anos < 10:
        aumento = sueldo * 0.05
        print("Aumento: ", aumento)
        print("nuevo sueldo:", sueldo + aumento)
    else: 
        if sueldo > 500:
            print("sueldo:",sueldo)

# 8-7 Escribir un programa: Dada una lista de 3 valores distintos, calcule su rango de variacion
# Mostrar el mayor y el menos de ellos
# Se utilizan las variables del primer ejemplo num1 num2 num3
            
if num1 > num2 and num1 > num3:
    print(num1,"es mayor")
else:
    if num2 > num3:
        print(num2,"es mayor")
    else:
        print(num3, "es mayor")

if num1 < num2 and num1 < num3:
    print(num1,"es menor")
else:
    if num2 < num3:
        print(num2,"es menor")
    else:
        print(num3,"es menos")