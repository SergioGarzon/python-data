variable_str = "Hola mundo"  # Str: Cadena de caracteres
variable_int = 10            # int: Numero entero
variable_float = 10.5        # float: Numero con coma flotante
variable_complex = 3 + 4j   # Complex: Numero complejo
variable_bool = False        # Bool: Valor logico
variable_tuple = ("Hola", "Hola", "Hola") # Tuple: Tupla
variable_list = ["Hola", 10, False]
variable_set = {"s", "e", "d"}
variable_nonetype = None

variable_dictionary = {   # Dict: Diccionario
  "Id": 1,
  "nombre": "Sergio",
  "apellido": "Ninguno"
}

print(type(variable_str))
print(type(variable_int))
print(type(variable_float))
print(type(variable_complex))
print(type(variable_bool))
print(type(variable_tuple))
print(type(variable_list))
print(type(variable_set))
print(type(variable_nonetype))
print(type(variable_dictionary))


# Range en Python range(start, stop, step)
print("Imprimimos rangos")

print("1)")
for i in range(5):
    print(i)

print("2)")
for i in range(3, 8):
    print(i)
    
print("3)")
for i in range(0, 10, 2):
    print(i)