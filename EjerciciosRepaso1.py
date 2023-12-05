# Estructuras condicionales simples y compuestas

# Ejercicio 1
num1=int(input("Ingrese primer valor:"))
num2=int(input("ingrese segundo valor:"))
print("El valor mayor es")
if num1>num2:
    print(num1)
else:
    print(num2)

# Ejercicio 2
num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))
if num1>num2:
    suma=num1+num2
    print("La suma de los dos valores es")
    print(suma)
    resta=num1-num2
    print("La diferencia de los dos valores es")
    print(resta)
else:
    producto = num1*num2;
    print("El producto de los dos valores es")
    print(producto)
    division = num1/num2;
    print("La división de los dos valores es")
    print(division)


"""
Problemas propuestos

Ejercicio 3: Se ingresan tres notas de un alumno, si el promedio es 
mayor o igual a siete mostrar un mensaje "Promocionado".

Ejercicio 4: Se ingresa por teclado un número positivo de uno o dos 
dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o 
dos dígitos.
(Tener en cuenta que condición debe cumplirse para tener dos dígitos 
un número entero)
"""