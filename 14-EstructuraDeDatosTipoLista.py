"""
# Hasta ahora hemos trabajado con variables que permiten almacenar un unico valor
edad =12
altura = 1.80
nombre = 'juan'

# Creacion de lista por asignacion
lista1 = [10, 5, 3] #lista de enteros
list2 = [1.78, 2.66, 1.55, 89.4] #lista de valores float
lista3 = ["lunes", "martes", "miercoles"] #lista de string
lista = ['juan', 45, 1.92] #lista de distintos elementos

print(len(lista1))

"""

# Problema 1
# Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma

lista = [10, 7, 3, 7, 2]
total = 0
for x in range(len(lista)):
    total =  total + lista[x]
print("El total de la suma de todos los elementos:",total)

# Problema 2
# Definir una lista por asignacion que almacene los nombre de los primeros 4 meses del ano.
# Mostrar el primer y ultimo elemento de la lista solamente

meses = ["enero", 'febrero', 'marzo', 'abril']
print(meses[0])
print(meses[-1])

# Definir una lista por asignacion que almacene en la primer componente elnombre de un alumno
# y en las 2 siguientes sus nota. Imprimir luego el nombre y el promedio
alumno = ['pepito', 8, 7]
print(alumno[0])
suma = (alumno[1] + alumno[2]) / 2
print(suma)