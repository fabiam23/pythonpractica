# Cuando se tienen listas paralelas y se ordenan los elementos de unas de ellas
# hay que tener la precaucion de intercambiar los elementos de las listas paralelas

# Problemas
# Confeccionar un programa que permita la carga de los nombre de 5 alumnos
# y sus notas respectivas. Luego ordenar las notas de mayor a menos
# Imprimir las notas y los nombres de los alumnos
# Debe quedar claro que cuando intercambiamos las notas para ordenarlas,
# debemos intarcambiar los nombres para que las listas continuen paralelas
    
"""
    
alumnos = []
notas = []

for x in range(5):
    alumno = input('Nombre del alumno: ')
    nota = int(input('Nota del alumno: '))
    
    alumnos.append(alumno)
    notas.append(nota)
    
print(alumnos)
print(notas)

for x in range(4):
    for z in range(4-x):
        if notas[z] > notas[z + 1]:
            auxN = notas[z]
            notas[z] = notas[z + 1]
            notas[z + 1] = auxN
            auxA = alumnos[z]
            alumnos[z] = alumnos[z + 1]
            alumnos[z + 1] = auxA
            
for x in range(5):
    print(alumnos[x], notas[x])
            
"""

# PROBLEMAS PROPUESTOS
# Crear y cargar una lista con los nombres de 5 paises y en otra la cantidad de habitantes
# Ordenar alfabeticamente e imprimir los resultados.
# Ordenar respecto a la cantidad de habitantes de mayor a menor

paises = []
habitantes = []

for x in range(5):
    pais = input('Nombre del pais: ')
    habitante = int(input('Cantidad de habitantes: '))
    
    paises.append(pais)
    habitantes.append(habitante)

print("")
for x in range(5):
    print(paises[x], habitantes[x])
           
print("") 

for x in range(len(paises)- 1):
    for p in range(4 - x):
        if paises[p] > paises[p + 1]:
            auxPais = paises[p]
            paises[p] = paises[p + 1]
            paises[p + 1] = auxPais
            auxHabit = habitantes[p]
            habitantes[p] = habitantes[p + 1]
            habitantes[p + 1] = auxHabit
            
for c in range(5):
    print(paises[c], habitantes[c])
    
print("")   
    
for x in range(len(paises)- 1):
    for p in range(4- x):
        if habitantes[p] < habitantes[p + 1]:
            auxPais = paises[p]
            paises[p] = paises[p + 1]
            paises[p + 1] = auxPais
            auxHabit = habitantes[p]
            habitantes[p] = habitantes[p + 1]
            habitantes[p + 1] = auxHabit
    
for c in range(5):
    print(habitantes[c], paises[c])
    
    