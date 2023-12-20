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
#se utilizan las variables del ejercicio anterio
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

#8-5 