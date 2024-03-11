"""
#Problema 1
def mostrar_mensaje(mensaje):
    print("******************************************")
    print(mensaje)
    print("******************************************")


def carga_suma():
    valor1 = int(input("Ingrese el prime valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    suma = valor1 + valor2
    print("La suma es:", suma)


#Programa principal
mostrar_mensaje("El programa calcula la suma de dos valores ingresados por el teclado")
carga_suma()
mostrar_mensaje("Gracias por utilizar este programa")

#Problema 2
#Confeccioar una funciona que reciba 3 enteros y nos muestre el mayor de ellos
#La Carga de los valores hacerlo por teclado

def mayor(v1, v2, v3):
    print("El mayor de los 3 valores es")
    if v1 > v2 and v1 > v3:
        print(v1)
    else:
        if v2 > v3:
            print(v2)
        else:
            print(v3)

def cargar():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    valor3 = int(input("Ingrese el tercer valor: "))
    mayor(valor1, valor2, valor3)


cargar()



#Problema 3
#Desarrollar un programa que permita ingresar el lado de un cuadrado. 
#Luego preguntar si quiere calcular y mostrar su perimetro o superficie.



def perimetro(lado):
    perimetro = lado * 4
    print("El Perimetro es:",perimetro)

def superficie(lado):
    superficie = lado * lado
    print("La superficie es: ",superficie)

def lado():
    valorLado = int(input("Ingrese el valor del lado: "))
    
    respuesta = input("Desea calcular el ['perimetro o superficie']: ")
    if respuesta == 'perimetro':
        perimetro(valorLado)
    elif respuesta=='superficie':
        superficie(valorLado)

lado()

"""

# PROBLEMAS PROPUESTOS

# Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales.
# Llamarla desde el bloque principal del programa 3 veces con string distintos.

def texto():

    for x in range(0,3):
        texto = input("Ingese el string: ")
        vocales(texto)


def vocales(cadena):
    cantidad = 0
    for x in range(len(cadena)):
        if cadena[x]=='a' or cadena[x]=='e' or cadena[x]=='i' or cadena[x]=='o' or cadena[x]=='u':
            cantidad = cantidad + 1
    
    print("La cantidad de vocales es: ",cantidad)


texto()