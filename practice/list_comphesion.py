list = [5, 88, 97, 91, 10, 15, 66, 77, 85, 11, 13, 22]

list_comphesion = [element ** 2 for element in list]

print(list_comphesion)

# With condicional

list_comphesion2 = [element ** 2 for element in list if element % 2 == 0]

print(list_comphesion2)