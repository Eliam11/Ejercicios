# Funciones extras para las listas

# Lista1 -Muestra CUANTOS elementos hay en la lista-
lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes",
         1, 2, 3, 4, 5, [1, 2, 3], True]
print(len(lista))

# Lista2 -Agregar nuevo elemento a la lista-
lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.append("Eliam")

# Lista3 -Insertar nuevo elemento en un indice especifico-
lista = [1, 2, 4, 5]
lista.insert(2, 3)
print(lista)

# Lista4 -Agrear una serie de elementos a una lsista-
lista = [1, 2, 3, 4, 5]
lista.extend([6, 7, 8])
print(lista)

# Lista5 -Concatenar diferentes listas-
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

# Lista6 -Saber si un elemento determinado esta en las listas-
lista = [1, 2, 3, 4, 5, "Eliam"]
print(3 in lista) #Ejemplo1
print("Eliam" in lista) #Ejemplo2
print(10 in lista) #Ejemplo3

# Lista7 -Retornar el valor del indice donde tengo el elemento guardado-
lista = [1, 2, 3, 4, 5, "Eliam"]
print(lista.index(5))

# Lista8 -Retorna cuantos valores exitentes hay repetidos-
lista = [1, 2, 3, 4, 5, "Eliam", 1, 2, 3, 4, 5, "Eliam"]
print(lista.count(1)) # Ejemplo1
print(lista.count("Eliam")) # Ejemplo2
print(lista.count(10)) # Ejemplo3

# Lista9 -Eliminar todos los elementos(y por indice tambien) segun el indice de la lista-
lista = [1, 2, 3, 4, 5, "Eliam"]
lista.pop() # Todos los elemtos
lista.pop(1) # Eliminar por indice especificado

# Lista10 -Eliminar valores de las listas-
lista = [1, 2, 3, 4, 5, "Eliam"]
lista.remove(5) # Elimina el valor '5' de la lista
lista.remove("Eliam")
lista.clear() # Elimina todos los valores de la lista
print(lista)

# Listas11 -Distintas funcionalidades de las listas-
#1 -Duplicar y revertir elementos-
lista.reverse() # Dar vuelta todos los elementos
lista = [1, 2, 3, 4, 5, "Eliam"] * 2 # Duplica los elementos de la lista
print(lista)
#2 -Ordenamiento de elementos(acendente y decendente)-
lista = [4, 5, 1, 4, 2, -1, -3]
lista.sort() # Acendente
print(lista)
lista.sort(reverse=True) # Decendente
print(lista)