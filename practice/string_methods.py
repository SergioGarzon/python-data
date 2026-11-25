name_person = "Micaela Hussein"

parameter = "Mic"
parameter_end = "ein"
parameter_position = "la"

print("Empieza con Mic" if name_person.startswith(parameter) else "No empieza con Mic")
print("Termina con ein" if name_person.endswith(parameter_end) else "No termina con ein")
print("La posicion en que se encuentra 'la' es: " + str(name_person.find(parameter_position)))

name_1 = "Sergio"
name_2 = "Barrera"

print(name_1.join(name_2)) # Output: BSergioaSergiorSergiorSergioeSergiorSergioa

new_string = name_1.replace("io", name_2)

print(new_string)

full_name = " Sergio Barrera "
print(full_name.strip())
print(full_name.split())
