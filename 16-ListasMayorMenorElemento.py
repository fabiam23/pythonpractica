# Para la comparacion de listas se necesita que ambas tengo valores del mismo valor, numeros numeros, string string, bool bool

"""

# Problema 1
# Crear y cargar una lista con 5 enteros. Implementar un algoritmo que me identifique el mayor de la lista
lista = []

for x in range(5):
    valor = int(input("Ingrese el valor: "))
    lista.append(valor)

mayor = lista[0]

for v in range(1, 5):
    if lista[v] > mayor:
        mayor = lista[v]
print('El mayor de los numeros de la lista:', mayor)


# Problema2
# Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor de la lista
# y la posicion donde se encuentra

lista = []

for x in range(5):
    valor = int(input("Ingrese el valor: "))
    lista.append(valor)

menor = lista[0]
posicion = 0
for x in range(1, 5):
    if lista[x] < menor:
        menor = lista[x]
        posicion = x

print('El menor valor es:', menor,'y su posicion es:',posicion)

"""

# PROBLEMAS PROPUESTOS

# Problema 1
# Ingresar por teclado 5 nombres de personas y almacenarlos en una lista
# Mostrar el nombre de persona menor en orden alfabetico

lista_Nombres = []


for x in range(5):
    nombre = input("Su nombre: ")
    lista_Nombres.append(nombre)

menor_nombre = lista_Nombres[0]
for p in range(1, 5):
    if lista_Nombres[p] < menor_nombre:
        menor_nombre = lista_Nombres[p]

print(lista_Nombres)
print(menor_nombre)