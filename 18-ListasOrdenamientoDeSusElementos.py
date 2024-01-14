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

# Problema 1
# Crear una lista y almacenar los nombre de 5 paises
# Ordenar alfabeticamente la lista e imprimirla

paises = []

for x in range(5):
    # Se le pasa la funcion lower para que todo sea miniscula y facil de comparar
    pais = input('Ingrese el pais: ').lower()
    paises.append(pais)
    
print(paises)

for x in range(4):
    for p in range(4-x):
        if paises[p] > paises[p + 1]:
            aux = paises[p]
            paises[p] = paises[p + 1]
            paises[p + 1] = aux


print(paises)



# Problema 2
# Solicitar por teclado la cantidad de empleados que tiene la empresa
# Crear y cargar una lista con todos los sueldos de dichos empleados
# Imprimir la lista de los sueldos ordenados de menor a mayor

empleados = int(input('Cuantos empleados tiene la empresa: '))
contador = 0
sueldos = []
while contador < empleados:
    valor = float(input('Sueldo: '))
    sueldos.append(valor)
    contador = contador + 1
    
print(sueldos)

for x in range(empleados - 1):
    for s in range(empleados -1 -x):#al usar len no se organiza
        if sueldos[s] > sueldos[s + 1]: 
            aux = sueldos[s]
            sueldos[s] = sueldos[s + 1]
            sueldos[s + 1] = aux
print(sueldos)

"""

# Problema 3
# Cargar una lista con 5 elementos enteros
# Ordenarla de menor a mayor y mostrar por pantalla
# Luego ordenar de mayor a menor e imprimirla

lista = []
