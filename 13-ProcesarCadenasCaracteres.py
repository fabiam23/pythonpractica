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

"""
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