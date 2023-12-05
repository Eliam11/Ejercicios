# Estructuraas condicionales anidadas

# Ejercicio 1
nota1=int(input("Ingrese primer nota:"))
nota2=int(input("Ingrese segunda nota:"))
nota3=int(input("Ingrese tercer nota:"))
prom=(nota1+nota2+nota3)/3
if prom>=7:
    print("Promocionado")
else:
    if prom>=4:
        print("Regular")
    else:
        print("Reprobado")

# Ejercicio 2
num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segunda valor:"))
num3=int(input("Ingrese tercer valor:"))
if num1>num2:
    if num1>num3:
        print(f"El valor mas grande es:{num1}")
    else:
        print(num3)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)

"""
Problemas propuestos

Ejercicio 1: Se ingresa por teclado un valor entero, mostrar una leyenda 
que indique si el número es positivo, negativo o nulo (es decir cero).

Ejercicio 2: Confeccionar un programa que permita cargar un número entero 
positivo de hasta tres cifras y muestre un mensaje indicando si tiene 
1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es 
mayor.

Ejercicio 3: Un postulante a un empleo, realiza un test de capacitación, 
se obtuvo la siguiente información: cantidad total de preguntas que se le 
realizaron y la cantidad de preguntas que contestó correctamente. Se pide 
confeccionar un programa que ingrese los dos datos por teclado e informe 
el nivel del mismo según el porcentaje de respuestas correctas que ha 
obtenido, y sabiendo que:

	Nivel máximo:	Porcentaje>=90%.
	Nivel medio:	Porcentaje>=75% y <90%.
	Nivel regular:	Porcentaje>=50% y <75%.
	Fuera de nivel:	Porcentaje<50%.
    
"""