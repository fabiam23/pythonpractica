#PRoblema 1

#Confeccionar una funcion que le enviemos como parametro el valor del lado de un 
#cuadrado y nos retorne su superficie

def retornar_superficie(lado):
    sup = lado * lado
    return sup


# Bloque principal del programa

va = int(input("Ingrese el valor del lado del cuadrado: "))
superficie = retornar_superficie(va)
print("La superficie del cuadrado es: ", superficie)