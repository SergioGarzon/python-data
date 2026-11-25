from functools import reduce

lista = [55, 69, 87, 11, 25, 23, 8, 57, 99]

sumatoria = reduce(lambda x, y: x + y, lista)


print("Lista original: " + str(lista))
print("Lista de sumatorias: " + str(sumatoria))

