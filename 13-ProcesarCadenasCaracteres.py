# Cadenas cargadas por asignacion y por teclado
"""
nombre = 'fabiam'
nombre1 = input("Cual es tu nombre: ")

# Operadores que se puede utilizar == igual, != desigual, < menor, <= menor igual, > mayor, >= mayor igual
# Como acceder a un caracter de un string o cadena
nombre = 'juan'
print(nombre[0])
if nombre[0] == 'j':
    print(nombre)
    print(len(nombre))
print('empieza con la letra j')

# Los subindices empiezan con la letra 0
# la funcion len devuelve el tamano de caracteres de un string


# Problema1 
# Realizar la carga del nombre de una persona y luego mostrar el primer caracter del nombre
# y la cantidad de letras que la componene

nombre = input("Ingrese su nombre: ")
print(nombre[0])
print(len(nombre))


# Problema2
# Solicitar la carga del nombre de una persona en minisculas.
# Mostrar un mensaje si comienza con vocal dicho nombre

nombre2 = input("Ingrese su nombre: ")
if nombre2[0] == 'a' or nombre2[0] == 'e' or nombre2[0] == 'i' or nombre2[0] == 'o' or nombre2[0] == 'u':
    print("su nombre empieza con una vocal")

# Problema3
# Ingresar un mail por teclado. Verificar si el string ingresado contiene un @
    
correo = input("Ingrese su correo: ")
for x in range(len(correo)):
    if correo[x] == '@':
        print('tiene @')

# Metodos propios de las cadenas
# upper() devuelve cadenas en mayusculas
# lower() devuelve cadenas en minisculas
# capitaliza() devuelve la primera letra en mayuscula

# Problema 4
# Inicializar un string con la Cadena mAriA, llamar los metodos upper, lower, capitalize
# guardarlos en otro string y mostrarlo en pantalla

nombre = "mAriA"
print(nombre)
nombre1 = nombre.upper()
print(nombre1)
nombre2 = nombre.lower()
print(nombre2)
nombre3 = nombre.capitalize()
print(nombre3)


# PROBLEMAS PROPUESTOS

# Problema1
# Cargar una oracion por teclado. Mostrar luego cuantos espacios en blanco se ingresaron.
# Tener en cuenta que un espacio en blanco es igual a " ", en cambio una cadena vacia es""

espacio = 0
oracion = input("Ingrese una oracion: ")

for n in range(len(oracion)):
    if oracion[n] == " ":
        espacio = espacio + 1
    print(n)
print("Cantidad de espacios en blanco:",espacio)

# Problema2
# Ingresar una oracion que puede tener letras mayusculas y minisculas.
# Contar la cantidad de vocales. Crear un string con toda la oracion en minisculas
# para que sea mas facil verificar que es una vocal
# Se toma el string del problema anterior

cadena2 = oracion.lower()
vocales = 0
for x in range(len(cadena2)):
    if cadena2[x] == "a" or cadena2[x] == "e" or cadena2[x] == "i" or cadena2[x] == "o" or cadena2[x] == "u":
        vocales = vocales +  1
        
print("Cantidad de vocales:",vocales)

"""
# Problema3
# Solicitar el ingreso de una clave por teclado y almacenarla. Controlar que el string tenga
# entre 10 y 20 caracteres para que sea valido, en caso contrario mostrar un mensase de error

clave = input("Ingrese la clave entre 10 y 20 caracteres: ")
if len(clave) < 10 or len(clave) > 20:
    print("error, la clave debe estar entre 10 y 20") 