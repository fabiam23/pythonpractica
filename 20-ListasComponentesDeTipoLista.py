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

"""

# Problema 2
# Crear una lista por asignacion. La lista tiene que tener 2 elementos. 
# Cada elemento debe ser una lista de 5 enteros.
# Calcular y mostrar la suma de cada lista contenida en el lista principal

lista = [[4,5,6], [3,5,9]]