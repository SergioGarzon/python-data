'''
Mascota de una veterinaria
Crear una clase Mascota con nombre, especie, edad y peso. Implementar el constructor y __str__(). Agregar un
método es_adulta() que determine si la mascota tiene 2 años o más y un método actualizar_peso(nuevo_peso) que
solamente permita asignar valores mayores que cero. Crear varias mascotas y almacenarlas en una lista
'''

def datos_mascota(mascota):
    print("Datos de la mascota")
    print(mascota)    
    print("Comprobamos si es viejito el animal")
    print("Es adulto/a" if mascota.es_adulta() else "No es adulto/a")

from Mascota import Mascota

list_mascota = []

valor = 0
edad = 0
peso = 0

try:
    valor = int(input("Desea insertar una nueva mascota? 1) Si, 2) No, ingrese opción: "))
except ValueError:
    valor = 0

while(valor != 0):        
    nombre = str(input("Ingrese el nombre de la mascota: "))
    especie = str(input("Ingrese la especie de la mascota: "))
    
    try:
        edad = int(input("Ingrese la edad de la mascota: "))
    except ValueError:
        edad = 0
     
    try:   
        peso = int(input("Ingrese el peso de la mascota: "))
    except ValueError:
        peso = 0
    
    mascota_nueva = Mascota(nombre, especie, edad, peso)
    list_mascota.append(mascota_nueva)
    
    try:
        valor = int(input("Desea insertar una nueva mascota? 1) Si, 2) No"))
    except ValueError:
        valor = 0
    

print("\nVerificamos los datos de la mascota: ")

for mascota in list_mascota:
    datos_mascota(mascota)
    resultado_pregunta = int(input("Desea actualizar el peso de la mascota? 1) Si 2) No"))
    if resultado_pregunta == 1:
        peso_nuevo = int(input("Ingrese el peso de la mascota: "))
        mascota.peso(peso_nuevo)
        print("Se ha actualizado el peso")
    else:
        print("No se ha actualizado el peso de la mascota")
    print(mascota)
    






