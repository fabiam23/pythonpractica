# Listas dentro de otra lista
"""
notas = [[4,5], [6,9], [7,3]]

# Problema1 
# Crear una lista por asignacion. La Lista tiene que tener cuatro elementos.
# Cada elemento debe ser una lista de 3 enteros.
# Imprimir sus elementos accediendo de diferentes modos

lista = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
# Se imprime la lista completa
print(lista)
print('=============')
# se imprime la primera componente
print(lista[0])
print('======')
for x in range(len(lista[0])):
    print(lista[0][x])
print('========')
for x in range(len(lista)):
    for p in range(len(lista[x])):
        print(lista[x][p])


# Problema 2
# Crear una lista por asignacion. La lista tiene que tener 2 elementos. 
# Cada elemento debe ser una lista de 5 enteros.
# Calcular y mostrar la suma de cada lista contenida en el lista principal

lista = [[4,5,6,6,3], [3,5,9,3,6]]
suma1 = lista[0][0] + lista[0][1]+ lista[0][2] + lista[0][3]+ lista[0][4]
suma2 = lista[1][0] + lista[1][1]+ lista[1][2] + lista[1][3]+ lista[1][4]

print(suma1)
print(suma2)
print('===================')

suma = 0
for x in range(len(lista[0])):
        suma = suma + lista[0][x]
print(suma)

suma1 = 0
for x in range(len(lista[1])):
        suma1 = suma1 + lista[1][x]
print(suma1)

print('*****************')

for x in range(len(lista)):
        sumando = 0
        for t in range(len(lista[x])):
                sumando = sumando + lista[x][t]
        print(sumando)
"""

# Problema 3
# Crear una lista por asignacion. La lista tiene que tener 5 elementos.
# Cada elemento debe ser una lista, la primera lista tiene que tener
# un elemento, la segunda 2, y la tercera 3 asi sucesivamente.
# Sumar todos los valores de las listas
