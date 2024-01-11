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

"""