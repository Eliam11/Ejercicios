# LISTAS: CARGA POR TECLADO DE SUS ELEMENTOS ---------------------------------
#Ejercicio 1
lista=[10,7,3,7,2]
suma=0
x=0
while x<len(lista):
    suma=suma+lista[x]
    x=x+1
print("Los elementos de la lista son")
print(lista)
print("La suma de todos sus elementos es")    
print(suma)

#Ejercicio 2
lista=["ana", 7, 9]
print("Nombre del alumno:")
print(lista[0])
promedio=(lista[1]+lista[2])//2
print("Promedio de sus dos notas:")
print(promedio)

#Ejercicio 3
lista=[1000, 6000, 400, 23, 130, 400, 60, 2000]
cantidad=0
x=0
while x<len(lista):
    if lista[x]>100:
        cantidad=cantidad+1
    x=x+1
    
print("La lista esta constituida por los elementos:")
print(lista)
print("La cantidad de valores mayores a 100 en la lista son:")
print(cantidad)

#Ejercico 4
lista=[8,1,9,2,10]
x=0
print("Elementos de la lista con valores iguales o superiores a 7")
while x<len(lista):
    if lista[x]>=7:
        print(lista[x])
    x=x+1

#Ejercicio 5
nombres=["juan", "ana", "marcos", "carlos", "luis"]
cantidad=0
x=0
while x<len(nombres):
    if len(nombres[x])>=5:
        cantidad=cantidad+1
    x=x+1

print("Todos los nombres son")
print(nombres)
print("Cantidad de nombres con 5 o mas caracteres")
print(cantidad)


# LISTAS: MAYOR Y MENOR ELEMENTO -----------------------
#Ejercicio 6
lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

mayor=lista[0]
for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]

print("Lista completa")
print(lista)
print("Mayor de la lista")
print(mayor)

#Ejercicio 7
lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

menor=lista[0]
posicion=0
for x in range(1,5):
    if lista[x]<menor:
        menor=lista[x]
        posicion=x

print("Lista completa")
print(lista)
print("Menor de la lista")
print(menor)
print("Posicion del menor en la lista")
print(posicion)

#Ejercicio 8
nombres=[]
for x in range(5):
    nom=input("Ingrese nombre de persona:")
    nombres.append(nom)

nombremenor=nombres[0]
for x in range(1,5):
    if nombres[x]<nombremenor:
        nombremenor=nombres[x]

print("La lista completa de nombres ingresado son")
print(nombres)
print("El nombre menor en orden alfabetico es:")
print(nombremenor)

#Ejercicio 9
lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

mayor=lista[0]
for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]

print("Lista completa")
print(lista)
print("Mayor de la lista")
print(mayor)

# contamos cuantas veces se encuentra el mayor en la lista
cantidad=0
for x in range(5):
    if lista[x]==mayor:
        cantidad=cantidad+1
if cantidad>1:
    print("El mayor se repite en la lista")

#LISTAS PARALELAS ---------------------------------------------
nombres=[]
edades=[]
for x in range(5):
    nom=input("Ingrese el nombre de la persona:")
    nombres.append(nom)
    ed=int(input("Ingrese la edad de dicha persona:"))
    edades.append(ed)

print("Nombre de las personas mayores de edad:")
for x in range(5):
    if edades[x]>=18:
        print(nombres[x])

#Ejercicio 10
productos=[]
precios=[]
for x in range(5):
    nom=input("Ingrese el nombre del producto:")
    productos.append(nom)
    pre=int(input("Ingrese el precio de dicho producto:"))
    precios.append(pre)

cantidad=0
for x in range(1,5):
    if precios[x]>precios[0]:
        cantidad=cantidad+1

print("Cantidad de productos con un precio mayor al primer producto ingresado")
print(cantidad)

#Ejercicio 11

nombres=[]
notas=[]
for x in range(4):
    nom=input("Ingrese nombre del alumno:")
    nombres.append(nom)
    no=int(input("Ingrese la nota de dicho alumno:"))
    notas.append(no)

cantidad=0
for x in range(4):
    print(nombres[x])
    print(notas[x])
    if notas[x]>=8:
        print("Muy Bueno")
        cantidad=cantidad+1
    else:
        if notas[x]>=4:
            print("Bueno")
        else:
            print("Insuficiente")

print("La cantidad de alumnos muy buenos son")
print(cantidad)

# Ejercicio 12
lista1=[]
print("Carga de la primer lista")
for x in range(4):
    valor=int(input("Ingrese valor:"))
    lista1.append(valor)

lista2=[]
print("Carga de la segunda lista")
for x in range(4):
    valor=int(input("Ingrese valor:"))
    lista2.append(valor)

listasuma=[]
for x in range(4):
    suma=lista1[x]+lista2[x]
    listasuma.append(suma)

print("Lista resultante:")
print(listasuma)