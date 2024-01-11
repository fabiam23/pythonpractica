# Una lista en python es mutable. Puede ir cambiando durante la ejecusion
"""
lista = [10, 20, 40]
print(len(lista))
lista.append(100)
print(len(lista))
print(lista[0])
print(lista[3])

# Problema 1
# Definir una lista vacia y luego solicitar la carga de 5 enteros por teclado 
# y agregarlos a la lista. Imprimir la lista generada

lista1 = []

contador = 0
while contador < 5:
    elemento = int(input('Ingrese un valor: '))
    lista1.append(elemento)
    contador = contador + 1
    
print(lista1)


# Problema 2
# Realizar la carga de valores enteros por teclado, almacenarlos en una lista.
# Finalizar la carga de enteros al ingresar 0. Mostrar el tamano de la lista

lista = []
valor = int(input('Ingrese el valor o (0) para finalizar: '))
while valor != 0:
    lista.append(valor)
    valor = int(input('Ingrese el valor o (0) para finalizar: '))
    
    
print('tamano de la lista',len(lista))


# PROBLEMA PROPUESTO
# Problema 1
# Almacenar en una lista los sueldos (decimal) de 5 operarios.
# Imprimir la lista y el promedio de los sueldos
suma = 0
sueldos = [105.50, 200.35, 140.35, 120.30, 190.50]
print(sueldos)
for x in range(len(sueldos)):
    suma = suma +sueldos[x]
    
promedio = suma / 5
print(promedio)
     
"""

# Problema 2
# Cargar por teclado y almacenaren una lista 5 alturas de personas
# Obtener el promedio. Contar cuantas personas son mas alta que el promedio y cuantas mas bajas

alturas = []

suma = 0
for x in range(5):
    valor = float(input('Ingrese su altura: '))
    alturas.append(valor)
    
    suma = suma + valor
    
promedio = suma / 5
print('Altura promedio:',promedio)

# Problema 3
