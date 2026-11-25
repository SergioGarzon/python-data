def print_list(data):
    print(data)

list_data = [1, 2, 3, True, "data input"]

print("Imprimimos los datos")
print_list(list_data)

print("\nAgregamos otro dato")
list_data.append(10.5)
print_list(list_data)

print("\nRemovemos el primer elemento")
list_data.remove(1)
print_list(list_data)

print("\nMostramos la longitud de la lista")
print(len(list_data))

print("\nArmamos una nueva lista con solo los elementos numericos")
numero1, numero2, *otros_datos, numero3 = list_data
list_new_data = [numero1, numero2, int(numero3)]
print(list_new_data)

print("\nOrdenamos la lista")
list_new_data.sort()
print(list_new_data)

print("\nInvertimos la lista")
list_new_data.reverse()
print(list_new_data)