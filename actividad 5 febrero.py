import random

#creacion de arreglo aleatorio de 50 elementos entre 1 y 100 con random.randint
my_array = [random.randint(1, 100) for _ in range(50)]
print("the array: ")
print(my_array)

#acceder al elemento en el indice 0
first_element = my_array[0]
print("the first element: ", first_element)
#indice24
element_24 = my_array[24]
print("the element in index 24: ", element_24)
#ulrimo elemento
last_element = my_array[-1]
print("the last element: ", last_element)



###Mini reto
#recorrer el arreglo y calcular la suma de todos los elementos
total_sum = sum(my_array)   
print("La suma es: ", total_sum) 

#insertar eleemento en el inicio del arreglo
new_element_start = random.randint(1, 100)
my_array.insert(0, new_element_start)
print("Nuevo elemento al inicio ", new_element_start)
print("Arreglo actualizado: ", my_array)

#insertar un nuevo elemento al final del arreglo
new_element = random.randint(1, 100)
my_array.append(new_element)
print("nuevo elemento agregado ", new_element)
print("Arreglo actualizado:", my_array)  


#eliminar un elemento intermedio del arreglo (por ejemplo, el elemento en el indice 10)
removed_element = my_array.pop(10)
print("elemento eliminado ", removed_element)
print("Arreglo actualizado: ", my_array)


#busscar un valor especifico en el arreglo 
search_value = 50
if search_value in my_array:
    index = my_array.index(search_value)
    print(f"El valor {search_value} se encuentra en el inidice {index}")
else:
    print(f"El valor {search_value} no se encuentra en el arreglo")