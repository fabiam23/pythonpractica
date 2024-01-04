#Comentarios en el Codigo fuente

"""Comentario varias lineas
no se ejecutan"""

# Mostrar la tabla del 5 con el ciclo while y con el ciclo for

x = 1

while x <= 10:
 print("5 *", x,"=", 5 * x)
 x = x + 1

 for p in range(1,11):
   print("5 *", p,"=", 5 * p)
 

 # PROBLEMAS PROPUESTOS
   
# Realizar un programa que solicite la carga de valores enteros por teclado y los sume
# Finalizar la carga cuando se digite el valor -1

total = 0
valor = 0

while valor != -1:
   
  total = total + valor
  valor = int(input("Ingrese un valor para acumular(digite -1 para finalizar): ")) 
print("La suma es:", total)


# Confeccionar un programa que solicite la carga de 10 valores reales por teclado
# Mostrar al final la suma
# Definir varias lineas de comentarios indicando el nombre del programa
# el programador y la fecha de modificaciones

# Desarrollador FabiamDev
# 04/01/2024

sumando = 0
for x in range(1,11):
  valor1 = int(input("Ingrese un valor: "))
  sumando = sumando + valor1

print("El acumulado es:", sumando)