# Functions with positional parameters

def saludo(nombre, apellido):
    print("Nombre: " + nombre + ", apellido: " + apellido)
        
saludo("Pablo", "Griego")


# Functions without one data

def saludo2(nombre, apellido = "Garcia"):
    print("Nombre: " + nombre + ", apellido: " + apellido)

saludo2("Rocio")


# Functions with unordered parameters
def saludo3(nombre, apellido):
    print("Nombre: " + nombre + ", apellido: " + apellido)
    
saludo3(apellido="Zerpa", nombre="Fabio")


# Functions with numbers sequency
def printNumbers(*numbers):
    cad = ""
    for number in numbers:
        cad += str(number) + ", "
        
    print(cad)
        
    
printNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# Functions with parameters "key - value"

def imprimir_datos(**datos):
    for clave, valor in datos.items():
        print(clave + ":", valor)

imprimir_datos(nombre="Juana", edad=25, ciudad="Pinamar")


# Functions with return

def sumar_numeros(numero1, numero2):
    return numero1 + numero2

print(sumar_numeros(10, 5))


