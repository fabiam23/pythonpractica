# Otro algoritmo muy comun que se debe conocer es el ordenamiento de una lista de datos

# Problema 1
# Se debe cargar unalista donde se almacenen 5 sueldos. 
# Desplazar el valor mayor de la lista a la ultima posicion.

"""

lista = []

for x in range(5):
    sueldo = int(input('Ingrese el sueldo: '))
    
    lista.append(sueldo)
    
print(lista)

valor = 0

for p in range(4):
    for x in range(4):
        if lista[x] > lista[x + 1]:
            valor = lista[x]
            lista[x] = lista[x+ 1]
            lista[x + 1]=valor
        
print(lista)

# PROBLEMAS PROPUESTOS

"""
# Problema 1
# 
