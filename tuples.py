numeric_tuple = (2, 3, 55, 998)

print(numeric_tuple)
print("Element: " + str(numeric_tuple[0]))
print("Element: " + str(numeric_tuple[1]))
print("Element: " + str(numeric_tuple[2]))
print("Element: " + str(numeric_tuple[3]))

print("Desestructuracion")
element0, element1, element2, element3 = numeric_tuple
print("Element: " + str(element0))
print("Element: " + str(element1))
print("Element: " + str(element2))
print("Element: " + str(element3))


alphabet_tuple = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "U", "V", "W", "X", "Y", "Z"

print("Datos de toda la tupla")
print(alphabet_tuple)

first_element, second_element, *other_tuple = alphabet_tuple

print(first_element)
print(second_element)
print(other_tuple)


